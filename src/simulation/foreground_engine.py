import os
import healpy as hp
import matplotlib.pyplot as plt
import numpy as np
import pysm3
import pysm3.units as u

# Ensure output directories exist
os.makedirs("data/interim", exist_ok=True)
os.makedirs("plots", exist_ok=True)

print("Step 1: Initializing PySM 3 Sky with d1 (Dust) and s1 (Synchrotron)...")
# Target NSIDE=512 to match Phase 1 perfectly
NSIDE = 512
sky = pysm3.Sky(nside=NSIDE, preset_strings=["d1", "s1"])

print("Step 2: Evaluating galactic foreground components at 150 GHz...")
target_frequency = 150 * u.GHz
foreground_maps = sky.get_emission(target_frequency)

# Use the correct top-level PySM function to get uK_RJ -> uK_CMB scaling factor
conversion_factor = pysm3.bandpass_unit_conversion(target_frequency, output_unit=u.uK_CMB)

# Extract the float factor to scale the naked numpy array values cleanly
scale = conversion_factor.value

t_foreground = foreground_maps[0].value * scale
q_foreground = foreground_maps[1].value * scale
u_foreground = foreground_maps[2].value * scale

print("Step 3: Regenerating pristine Phase 1 maps...")
try:
    # Try to load the text arrays if they exist
    cl_tt = np.loadtxt("data/raw/cl_tt.txt")
    cl_ee = np.loadtxt("data/raw/cl_ee.txt")
    cl_bb = np.loadtxt("data/raw/cl_bb.txt")
    cl_te = np.loadtxt("data/raw/cl_te.txt")
    cl_input = [cl_tt, cl_ee, cl_bb, cl_te]
    print("   -> Successfully loaded raw power spectra from data/raw/!")
except Exception:
    print("   -> Text files not found. Computing pristine CMB power spectra via CAMB directly inline...")
    import camb
    
    # Configure the exact standard baseline parameters from Phase 1
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0)
    pars.WantTensors = True
    pars.InitPower.set_params(As=2e-9, ns=0.965, nt=0.0, r=0.05)
    pars.set_for_lmax(2500, lens_potential_accuracy=0)
    
    # Calculate results
    results = camb.get_results(pars)
    cl_matrix = results.get_total_cls(lmax=2500, CMB_unit="muK", raw_cl=True)
    
    # Separate vectors
    cl_tt = cl_matrix[:, 0]
    cl_ee = cl_matrix[:, 1]
    cl_bb = cl_matrix[:, 2]
    cl_te = cl_matrix[:, 3]
    cl_input = [cl_tt, cl_ee, cl_bb, cl_te]
    
    # Save them now so they are there for the future smoke test
    os.makedirs("data/raw", exist_ok=True)
    np.savetxt("data/raw/cl_tt.txt", cl_tt)
    np.savetxt("data/raw/cl_ee.txt", cl_ee)
    np.savetxt("data/raw/cl_bb.txt", cl_bb)
    np.savetxt("data/raw/cl_te.txt", cl_te)
    print("   -> Pristine Cl arrays successfully calculated and cached to data/raw/.")

# Synthesize the pristine sky fields using healpy
print("   -> Synthesizing pristine sky fields...")
t_pristine, q_pristine, u_pristine = hp.synfast(cl_input, nside=NSIDE, new=True, pixwin=True)

print("Step 4: Co-adding maps to create 'Dirty Datasets'...")
t_dirty = t_pristine + t_foreground
q_dirty = q_pristine + q_foreground
u_dirty = u_pristine + u_foreground

print("Step 5: Saving dirty maps to data/interim/...")
hp.write_map("data/interim/dirty_t_map.fits", t_dirty, overwrite=True)
hp.write_map("data/interim/dirty_q_map.fits", q_dirty, overwrite=True)
hp.write_map("data/interim/dirty_u_map.fits", u_dirty, overwrite=True)

print("Step 6: Visualizing Dirty Full-Sky Maps...")
# Visualizing Temperature Contamination
hp.mollview(t_dirty, title="Dirty CMB Temperature Map (T) at 150 GHz", cmap="jet", unit=r"$\mu$K")
plt.savefig("plots/dirty_temperature_map.png", dpi=300)

# Visualizing Polarization Contamination
hp.mollview(q_dirty, title="Dirty CMB Polarization Map (Q) at 150 GHz", cmap="jet", unit=r"$\mu$K")
plt.savefig("plots/dirty_q_polarization_map.png", dpi=300)

plt.show()
print("Phase 2 Generation Complete! Ready for Smoke Test.")