Functional Benchmarking
============

Overview
-------

"The right answer for the right reason at the right price." John P. Perdew

what functional to use? 

* Need to balance **physical accuracy** with **computational cost**.

Need to focus on properties of interest.

 * Binding energies
 * Reaction barriers
 * Vibrational frequencies
 * TS geometries
 * Minimum energy geometries

* Things to consider when benchmarking (1)
 * Is data directly comparable to ab initio (temp, pure sample, etc)
 * Is data diverse
 * What are the error bars for experimental measurements?
 * Use several sources to prevent bias 

How do we address the physical phenomena that influence performance of real catalyst that are not included in DFT calculations?
Do we need to worry about self-interaction errors? ( hybrid functionals can partially correct for this) 
Does our system have strong electron correlation?

* Known Systems with self-interaction errors (2)
 * actinides
 * various transition-metal oxides that have partially filled d or f shells

Magnesium is a group 2 alkaline earth metal ( electron configuration [Ne] 3s2)

However in MgO, we are interested in the impact of oxygen vacancies and different substitutions of Pt. These systems should be explored for strong electron correlation


Properties - Physical Accuracy
-------

Need to quantify how accurate DFT predictions are for specified property of interest.

Types of functionals
----------

* **LDA** - Local Density Approximation
 * exchange-correlation energy at any point in space is a function of the electron density at that point in space only (hence local) and can be given by the electron density of a homogeneous electron gas of the same density (homogeneous gases have already been calculated)
 * Tends to overestimate binding energies
 * Typically underestimates exchange and ovestimates correlation (helps errors cancel)
* **LSDA** - Local spin density approximation
 * General application of LDA which includes spin dependence
* **GGA** - Generalized Gradient Approximation
 * Includes local density and the gradient of the density
 * Accounts for inhomogeneous varying nature of electron density
 * two broad classes of GGAs:
 #. **Emperical** - Fitted to large training sets
 #. **Non-Emperical** - Derived from first principles using constraints known from quantum mechanics
* **Meta-GGA**
 * Includes higher order density gradients 
 * includes the orbital kinetic energy density
* **Hybrids**
 * Combine exact exhange from Hartree-Fock with GGA method
 * Optimizing functional fitting coefficients is usually performed on experimental data
* **Hybrid-metta GGA**
 * Hybrid mixed with meta GGA

Functional Selection
-------------


B3LYP
-------

SCAN 
----------



BEEF-vdw
----------

References
--------

#. https://youtu.be/Ey00F_vsIiY (Benchmarking DFT and beyond-DFT methods for thermodynamics and electronic properties - Geoffroy Hautier)

#. General Performance of Density Functionals Sérgio Filipe Sousa, Pedro Alexandrino Fernandes, and Maria João Ramos The Journal of Physical Chemistry A 2007 111 (42), 10439-10452 DOI: 10.1021/jp0734474

#. https://youtu.be/03Y0v4Ys3_A (SCAN meta-GGA: predictive power of 17 constraints)



