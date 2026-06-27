import camb
import healpy as hp
import matplotlib.pyplot as plt
import numpy as np

print("Step 1: Setting up the cosmological parameters")
pars = camb.CAMBparams()
# Base cosmology matching Planck baselines
pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0)
pars.InitPower.set_params(As=2e-9, ns=0.965)

# CRITICAL FIX 1: Enable Tensors and set r = 0.05 for Hypothesis 2
# Enable Tensors and set parameters all in one action
pars.WantTensors = True
pars.InitPower.set_params(As=2e-9, ns=0.965, nt=0.0, r=0.05)

# Set multipole range (lmax=2500 for the high-l tail to test Hypothesis 1)
pars.set_for_lmax(2500, lens_potential_accuracy=1)

# Get results
results = camb.get_results(pars)
# Extract raw and unscaled C_l arrays (0=TT, 1=EE, 2=BB, 3=TE)
# This includes both lensed scalars and the injected r=0.05 primordial tensors
cl_matrix = results.get_total_cls(lmax=2500, CMB_unit="muK", raw_cl=True)

cl_tt = cl_matrix[:, 0]
cl_ee = cl_matrix[:, 1]
cl_bb = cl_matrix[:, 2]
cl_te = cl_matrix[:, 3]
# Transpose/stack them into the exact format healpy.synfast expects for polarization
cl_templitude = np.array([cl_tt, cl_ee, cl_bb, cl_te])

print("Step 2: Simulating a pristine sky map (T, Q, U) from the physics")
# NSIDE=512 to accomodate Surface Pro 7 memory limit lmax=2500
NSIDE = 512

# CRITICAL FIX 3: Passing all 4 spectra outputs 3 maps: Temperature, Q-polarization, U-polarization
t_map, q_map, u_map = hp.synfast(cl_templitude, nside=NSIDE, new=True)

print("Step 3: Plotting the simulated universe maps")
# Plot Temperature Map
hp.mollview(
    t_map,
    title="Pristine CMB Temperature Fluctuations (T)",
    cmap="jet",
    unit=r"$\mu$K",
)

# Plot Q-Mode Polarization Map
hp.mollview(
    q_map,
    title="Pristine CMB Polarization Map (Q)",
    cmap="jet",
    unit=r"$\mu$K",
)

plt.show()

print("Phase 1 Base Engine Executed Successfully!")