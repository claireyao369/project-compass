# Project COMPASS

Cosmic Oscillation and Multipole Parameter Analysis via Separated Signals. 

## Central Research Question
How can an automated component separation pipeline—using Machine Learning for non-linear galactic foreground removal—isolate CMB B-mode polarization to simultaneously constrain the primordial tensor-to-scalar ratio (r) and test for large-scale deviations from Einsteinian General Relativity via gravitational lensing signatures?

## Two-Part Hypothesis
*   **Hypothesis 1 (The Structural Framework):** If large-scale structural growth deviates from the predictions of Einsteinian General Relativity due to modified gravitational physics on cosmological scales, then the rate of gravitational lensing will anomalously affect the CMB polarization fields. Specifically, the conversion of primordial E-modes into secondary, lensing-induced B-modes at high multipoles ($1000 < \ell < 2000$) will yield a structure growth index ($\gamma \neq 0.55$) or a gravitational slip parameter ($\eta \neq 1$), mathematically invalidating the standard $\Lambda\text{CDM}$ gravitational framework in favor of a Modified Gravity model (e.g., $f(g)$ or scalar-tensor theories).
*   **Hypothesis 2 (The Quantum Origin and the Inflation):** If the early universe underwent a phase of rapid cosmic inflation driven by a scalar field, then the resulting primordial tensor perturbations (gravitational waves) will imprint a curl-like polarization pattern onto the CMB. By isolating the pristine B-mode angular power spectrum ($C_\ell^{BB}$) at low multipoles ($\ell < 100$), an MCMC statistical analysis will constrain the tensor-to-scalar ratio to a non-zero value ($r > 0$), establishing the definitive energy scale of inflation and validating Grand Unified Theories (GUT).

## Research Pillars & Potential Breakthroughs

### Pillar 1: The Quantum Origin (B-mode and Inflation)

#### **Overview**
*   **Target:** Extreme large-scale features of the universe (low multipoles, $\ell < 100$).
*   **Method:** Uses the cleanest parts of the AI-separated B-mode map to look for the echo of the Big Bang.
*   **Objective:** Measure the energy scale of creation before matter even existed.

#### **Explanation**
*   If the universe expanded faster than the speed of light in its first trillionth of a second, that growth creates ripples in spacetime $\rightarrow$ **primordial gravitational waves**.
*   These waves leave a swirling pattern in the polarization of the CMB light.
*   Finding these ripples will prove that cosmic inflation really happened.

#### **Research Direction**
*   Feed the ML-cleaned B-mode map into the MCMC sampler to isolate the low- $\ell$ spectrum.
*   The code will search for a statistical boundary on the variable $r$ (**tensor-to-scalar ratio**), which measures how powerful those gravitational ripples were compared to standard density ripples.

#### **The Verdict**
*   **If $r > 0$:** Validated Grand Unified Theories (GUT) of particle physics, proving Cosmic Inflation happened, and establishing the exact energy scale of the universe's birth ($\sim 10^{16}\text{ GeV}$).
*   **If $r = 0$:** Rejected the inflation model, forcing modern cosmology to look for an alternative early-universe mechanism theory (e.g., cyclic/ekpyrotic models).

---

### Pillar 2: The Structural Framework (Modified Gravity)

#### **Overview**
*   **Target:** Ultra-fine, microscopic details of the universe (high multipoles, $1000 < \ell < 2000$).
*   **Method:** Looks at how the straight lines of ancient light were bent and distorted across the universe.

#### **Explanation**
*   Light travels through a universe filled with a web of dark matter.
*   According to Einstein, mass warps spacetime.
*   As standard, straight CMB light patterns (E-modes) pass through these gravitational lenses, they get physically twisted into a secondary type of swirl (**lensing-induced B-modes**).
*   By measuring how these lights are twisted, we can check if Einstein's law of gravity holds true on a cosmic scale.

#### **Research Direction**
*   Analyze the fine-grained, high- $\ell$ tail of the B-mode spectrum.
*   The MCMC engine will test these lensing signatures against models of gravity beyond General Relativity to constrain two critical parameters:
    *   $\gamma$ (the structure growth index)
    *   $\eta$ (the gravitational slip parameter)

#### **The Verdict**
*   **If $\gamma = 0.55$ and $\eta = 1$:** General Relativity is verified as the absolute law of the cosmos, meaning that Dark Energy must be a static Cosmological Constant ($\Lambda$).
*   **If $\gamma \neq 0.55$ or $\eta \neq 1$:** Standard gravity is invalid, therefore favoring the existence of a Modified Gravity theory (e.g., $f(R)$ gravity or scalar-tensor frameworks).

## Roadmap and Phases

### Pre-Pipeline Phases

#### **Phase 0: Ideas and Foundations**
*   Master the core physics concepts.
*   Come up with the fundamental project outline (central research questions, two-part hypothesis, roadmap).
*   Set up the whole framework on GitHub.
*   *Expected:* A full project outline on OneNote, README completed on GitHub.

#### **Phase 0.25: Research Core Physics**
*   Research concepts regarding both pillars:
    *   Acoustic oscillations
    *   Polarization tensors
    *   E/B mechanics
    *   Multi-variable calculus
    *   Multi-variable statistics
*   *Expected:* All the basic physics research is filled up.

#### **Phase 0.5: Building the Environment**
*   Build the local coding environment (Anaconda, cosmology environment, fix initial scaling bugs).
*   *Expected:* Have a well-established working environment, have an initialized cosmology environment for Python, and OneNote is all good to go.

---

### The Technical Pipeline

#### **Phase 1: Primordial Physics System (Base Engine)** — *Generate a perfect universe*
*   Have a math model (maybe in LaTeX or on OneNote) of the scripts to calculate the simulated pristine CMB.
*   Done through calculations of the theoretical linear perturbation equations of the early universe, outputting pristine, noise-free full-sky temperature (TT), E-mode (EE), and lensed/unlensed B-mode (BB) angular power spectra.
*   Generated the perfect universe on the computer based on the laws of physics (gives a clean baseline to test theories).
*   *Expected:* Normalized, pristine HEALPix maps showing the primordial universe at micro-Kelvin ($\mu\text{K}$) resolution scales.

#### **Phase 2: Interstellar Foreground Contamination** — *Slightly alter the universe map*
*   Use Python `sky model` to simulate real-world thermal galactic dust and synchrotron radiation fields from our Milky Way, superimposing them over the perfect universe maps.
*   Alter the changes a small amount each time (Ex. 1%, 2%, 3%, ...).
*   Intentionally ruin the perfect universe maps by putting space dust and alterations over them, simulating realistic data puzzles.
*   *Expected:* A massive folder of highly contaminated dirty universe maps to mimic what real-world observatories retrieved.

#### **Phase 3: Non-Linear Component Separation (The ML Highlight)** — *Train the AI and deploy into the real world*
*   Make an AI (using a Convolutional Autoencoder, or a U-Net adapted for spherical HEALPix pixels) in PyTorch/TensorFlow.
*   Use the massive library from Phase 2 to train the AI to identify dust signatures and isolate the B-mode map underneath.
*   Training an AI to act as an advanced digital stain-remover. It will look at the dusty map, figure out dust vs. deep space, and then scrub the dust away.
*   Then put the trained AI into the real-world data map from space telescopes (ex. JWST, Planck) to perform real-world non-linear component separation.
*   *Expected:* A trained AI model, a cleaned 2D B-mode map.

#### **Phase 4: Power Spectrum & Scale Decomposition** — *Turn cleaned-map into 1D angular power spectrum*
*   Transform the cleaned 2D map into a 1D angular power spectrum graph ($C_\ell^{BB}$).
*   Divide this data array into two distinct zones:
    *   **Low-$\ell$ peaks:** Targets Quantum Origin, large-scaled features.
    *   **High-$\ell$ tails:** Target structural frameworks, fine-grained details.
*   Turn visual maps into a line graph and scan it like a barcode, then split it into two zones so the details can be better analyzed.
*   *Expected:* A 1D angular power spectrum curve plot split into the two pillar zones.

---

### Statistical Analysis (Validation and the Verdict)

#### **Phase 5: MCMC Statistical Validation**
*   Run a Markov Chain Monte Carlo (MCMC) sampler to compare the power spectrum from Phase 4 with actual historical cosmic data (ex. Planck satellite data).
*   The sampler will run thousands of simulations to calculate the exact error bars.
*   The computer tests thousands of mathematical combinations to calculate the exact margin of error, proving the results are scientifically valid.
*   *Expected:* Corner plots showing the precise probability distribution and error bars of the results.

#### **Phase 6: Cosmological Parameter Estimation (The Moment of Truth! The Verdict)**
*   Extract the final mathematical values for the parameters.
*   Check if the tensor-to-scalar ratio is greater than 0 ($r > 0$) for Pillar 1.
*   Evaluate if the structure growth index ($\gamma$) deviates from 0.55 for Pillar 2.
*   Reading the final values, we mathematically determine if Einstein's theories are right, and discover how powerful Cosmic Inflation is.

---

### The Grande Finale

#### **Phase 7: Paper Writing and Conclusion**
*   Write a formal scientific paper, conclude the GitHub repository, and make presentable outreach for presentations.
