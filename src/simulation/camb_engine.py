import camb
import healpy as hp
import matplotlib.pyplot as plt
import numpy as np

print("Step 1: Setting up the cosmological parameters...")
pars = camb.CAMBparams()
pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0)
pars.InitPower.set_params(As=2e-9, ns=0.965)
pars.set_for_lmax(2500, lens_potential_accuracy=0)

results = camb.get_results(pars)
# UPDATED LINE BELOW
powers = results.get_cmb_power_spectra(pars, CMB_unit="muK")
totCL = powers["total"]
cl_tt = totCL[:, 0]

print("Step 2: Simulating a pristine sky map from the physics...")
NSIDE = 512
pristine_map = hp.synfast(cl_tt, nside=NSIDE)

print("Step 3: Plotting the simulated universe")
hp.mollview(
    pristine_map,
    title="Pristine Simulated Cosmic Microwave Background",
    cmap="planck",
    unit="K",
)
plt.show()