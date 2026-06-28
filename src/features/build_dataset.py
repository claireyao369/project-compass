import os
import healpy as hp
import numpy as np
import pysm3
import pysm3.units as u

# Setup clean directory tracks
os.makedirs("data/processed/train/inputs", exist_ok=True)
os.makedirs("data/processed/train/targets", exist_ok=True)

NSIDE = 512
N_PATCHES = 100

print("Step 1: Initializing base cosmological models...")
# Initialize PySM sky model
sky = pysm3.Sky(nside=NSIDE, preset_strings=["d1", "s1"])
conversion_factor = pysm3.bandpass_unit_conversion(150 * u.GHz, output_unit=u.uK_CMB).value

# Load or inline compute baseline pristine power spectra vectors from Phase 2
try:
    cl_tt = np.loadtxt("data/raw/cl_tt.txt")
    cl_ee = np.loadtxt("data/raw/cl_ee.txt")
    cl_bb = np.loadtxt("data/raw/cl_bb.txt")
    cl_te = np.loadtxt("data/raw/cl_te.txt")
except Exception:
    import camb
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0)
    pars.WantTensors = True
    pars.InitPower.set_params(As=2e-9, ns=0.965, r=0.05)
    pars.set_for_lmax(2500, lens_potential_accuracy=0)
    results = camb.get_results(pars)
    cl_matrix = results.get_total_cls(lmax=2500, CMB_unit="muK", raw_cl=True)
    cl_tt, cl_ee, cl_bb, cl_te = cl_matrix[:, 0], cl_matrix[:, 1], cl_matrix[:, 2], cl_matrix[:, 3]

cl_input = [cl_tt, cl_ee, cl_bb, cl_te]

print("\nStep 2: Generating raw Galactic Foreground models...")
fg_maps = sky.get_emission(150 * u.GHz)
t_fg = fg_maps[0].value * conversion_factor
q_fg = fg_maps[1].value * conversion_factor
u_fg = fg_maps[2].value * conversion_factor

# Convert raw foreground maps to coordinate-independent E and B modes to fix coordinate problem
fg_eb = hp.map2alm([t_fg, q_fg, u_fg], lmax=1000, pol=True)
_, e_fg_map, b_fg_map = hp.alm2map(fg_eb, nside=NSIDE, pol=True)

print(f"\nStep 3: Starting Factory Loop to generate {N_PATCHES} training patches...")

# Define pointing coordinates across a grid on the sky away from the blindingly pure white core center
# but close enough to capture realistic dust gradients
ra_centers = np.linspace(0, 360, N_PATCHES)
dec_centers = np.linspace(-30, 30, N_PATCHES)

for i in range(N_PATCHES):
    # 1. Synthesize a unique pristine cosmic realization
    t_p, q_p, u_p = hp.synfast(cl_input, nside=NSIDE, new=True, pixwin=True, verbose=False)
    p_eb = hp.map2alm([t_p, q_p, u_p], lmax=1000, pol=True)
    _, e_p_map, b_p_map = hp.alm2map(p_eb, nside=NSIDE, pol=True)
    
    # 2. Inject a variable alteration scaling factor (gradient from 5% to 100% dust threat)
    scaling = 0.05 + (0.95 * (i / N_PATCHES))
    
    # Co-add in pure E and B space!
    e_dirty_map = e_p_map + (e_fg_map * scaling)
    b_dirty_map = b_p_map + (b_fg_map * scaling)
    
    # 3. Project to flat 2D images using Gnomonic Projection (resolving Spherical Convolutions)
    # Target size: 256x256 pixels covering a 10-degree patch of deep space
    dirty_patch = hp.gnomview(b_dirty_map, rot=[ra_centers[i], dec_centers[i]], 
                             reso=2.34, xsize=256, return_projected_map=True, no_plot=True)
    
    target_patch = hp.gnomview(b_p_map, rot=[ra_centers[i], dec_centers[i]], 
                              reso=2.34, xsize=256, return_projected_map=True, no_plot=True)
    
    # 4. Extract raw data from the MaskedArray, replacing any empty border pixels with 0.0
    dirty_patch_filled = np.ma.filled(dirty_patch, fill_value=0.0)
    target_patch_filled = np.ma.filled(target_patch, fill_value=0.0)
    
    # Save clean/dirty numpy array twins directly to disk
    np.save(f"data/processed/train/inputs/dirty_{i:03d}.npy", dirty_patch_filled.astype(np.float32))
    np.save(f"data/processed/train/targets/clean_{i:03d}.npy", target_patch_filled.astype(np.float32))
    
    if (i + 1) % 10 == 0:
        print(f"   -> Progress: {i + 1}/{N_PATCHES} dataset pairs compiled successfully.")

print("\nDataset generation fully complete! Check data/processed/train/ folders.")