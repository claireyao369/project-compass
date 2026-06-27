import os
import healpy as hp
import matplotlib.pyplot as plt
import numpy as np

print("Step 1: Loading 'Dirty' maps from data/interim/...")
try:
    t_dirty = hp.read_map("data/interim/dirty_t_map.fits", field=0)
    q_dirty = hp.read_map("data/interim/dirty_q_map.fits", field=0)
    u_dirty = hp.read_map("data/interim/dirty_u_map.fits", field=0)
except Exception as e:
    print(f"Error loading dirty maps: {e}")
    exit()

print("Step 2: Loading pristine numerical power spectra from data/raw/...")
cl_tt_pristine = np.loadtxt("data/raw/cl_tt.txt")
cl_ee_pristine = np.loadtxt("data/raw/cl_ee.txt")
cl_bb_pristine = np.loadtxt("data/raw/cl_bb.txt")

print("Step 3: Running hp.anafast to extract contaminated power spectra...")
# hp.anafast extracts TT, EE, BB, TE, EB, TB from map arrays
cl_dirty = hp.anafast([t_dirty, q_dirty, u_dirty], lmax=2000)

cl_tt_dirty = cl_dirty[0]
cl_ee_dirty = cl_dirty[1]
cl_bb_dirty = cl_dirty[2]

# Create an array of multipoles (l) for plotting
ell_pristine = np.arange(len(cl_tt_pristine))
ell_dirty = np.arange(len(cl_tt_dirty))

print("Step 4: Generating mathematical verification plot...")
plt.figure(figsize=(10, 6))

# Plot B-modes (The ultimate target for our ML network)
plt.plot(ell_pristine, ell_pristine*(ell_pristine+1)*cl_bb_pristine / (2*np.pi), 
         label="Pristine Primordial B-modes (Target)", color="indigo", linestyle="--", linewidth=2)
plt.plot(ell_dirty, ell_dirty*(ell_dirty+1)*cl_bb_dirty / (2*np.pi), 
         label="Dirty Corrupted B-modes (Observed)", color="crimson", alpha=0.8)

# Format the plot scientifically
plt.yscale("log")
plt.xlim(2, 500)  # Zoom in on the low-multipole regime where dust dominates
plt.xlabel(r"Multipole Moment ($\ell$)", fontsize=12)
plt.ylabel(r"$\ell(\ell+1)C_\ell / 2\pi$ [$\mu$K$^2$]", fontsize=12)
plt.title("Phase 2 Smoke Test: Primordial B-Mode Foreground Swamping", fontsize=14)
plt.grid(True, which="both", linestyle=":", alpha=0.5)
plt.legend(fontsize=11, loc="upper right")

# Save and show
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/smoke_test_validation.png", dpi=300)
print("Plot saved to plots/smoke_test_validation.png")
plt.show()