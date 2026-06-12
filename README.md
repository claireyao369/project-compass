# Project COMPASS
**Cosmic Oscillations & Multipole Parameter Analysis via Separated Signals**
A documentation of building a project involving an advanced ML/MCMC pipeline for CMB component separation, Hubble Tension resolution, and modified gravity testing.

---

## Abstract
Project COMPASS addresses three critical questions in modern $$\lambda$$ CDM cosmology: the **Hubble Tension**, the nature of **relativistic degrees of freedom ($N_{\text{eff}}$)**, and potential large-scale deviations from **Einsteinian General Relativity**. 

By engineering an automated component separation pipeline that leverages non-linear Machine Learning architectures (CNNs/Autoencoders), COMPASS isolates primordial $B$-mode polarization signatures and high-multipole temperature anisotropies from heavily contaminated Interstellar Medium (ISM) dust and synchrotron foregrounds. The reconstructed cosmic microwave background (CMB) power spectra are  evaluated using Markov Chain Monte Carlo (MCMC) statistical sampling to constrain non-standard cosmological parameters ($r$, $N_{\text{eff}}$, $w(a)$, and $\gamma$).

---

## Research Roadmap & Architecture
The project consists of six phases, connecting theoretical reasoning and statistical simulations:
1. **Phase 1: Primordial Physics Simulation (Base Engine):** Generation of pristine unlensed and lensed CMB temperature ($TT$) and polarization (EE/BB) angular power spectra using `CAMB`.
2. **Phase 2: Interstellar Foreground Contamination:** Superimposition of non-linear galactic dust thermal emissions and synchrotron radiation utilizing the Python Sky Model (`PySM3`).
3. **Phase 3: Non-Linear Component Separation (ML Highlight):** Deep learning-driven foreground extraction to isolate the deep-sky primordial $B$-mode signatures.
4. **Phase 4: Power Spectrum & Fast Emulation:** Rapid extraction of high- $\ell$ damping tails and mapping of gravitational lensing anomalies via neural network parameter emulators (ML).
5. **Phase 5: MCMC Cross-Validation:** Robust likelihood exploration and parameter constraint mapping via Bayesian MCMC samplers (`emcee`/`Cobaya`) benchmarked against legacy Planck and ACT data.
6. **Phase 6: Cosmological Interpretation:** Mathematical evaluation of Dark Energy evolution equations of state ( $w(a)$ ) and Modified Gravity structure growth coefficients.
