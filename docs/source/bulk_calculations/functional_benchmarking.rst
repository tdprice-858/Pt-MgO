Functional Benchmarking
============

Overview
-------

"The right answer for the right reason at the right price." John P. Perdew

what functional to use? 

* Need to balance **physical accuracy** with **computational cost**.
* Also want to make sure trends are correct

Need to focus on properties of interest.

 * Binding energies
 * Reaction barriers
 * Reaction energetics (gibbs free energy changes)
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
 *known to overestimate the adsorption energies of molecules on transition metals
* **Meta-GGA**
 * Includes higher order density gradients 
 * includes the orbital kinetic energy density, which is computed from orbitals that are functionals of the density
 * Due to inclusion of orbital kinetic energy density with electron density and its gradients, meta-GGAs have more flexibilty
* **Hybrids**
 * Combine exact exhange from Hartree-Fock with GGA method
 * Optimizing functional fitting coefficients is usually performed on experimental data
* **Hybrid-metta GGA**
 * Hybrid mixed with meta GGA
* **ONIOM** - Our own n-layered Integrated molecular Orbital and Molecular mechanics
 * Computational hybrid method that enables different ab initio or semi-empirical methods to be applied to different parts of a molecule/system in combination to produce reliable geometry and energy at reduced computational cost
 * Can combine different functions like (PBE/HSE)

Functional Selection
-------------

LDA
-----

B3LYP
-------

* Contains a portion of Hartree-Fock exchange and cannot be used on solids

PBE - Perdew-Burke-Ernzerhof
------------
Constructed to satisfy 11 exact constraints. 

RPBE - Revised Perdew-Burke-Ernzerhof
---------

PBEsol
-------

SCAN - Strongly Constrained and Appropriately Normed Semilocal Density Functional 
----------

SCAN was constructed by Perdews team and is the first meta-GGA that is fully constrained to all 17 known exact constraints that a semi-local function can satisfy 

It is not fitted to any bonded system. It is fitted to norms, non-bonded systems such as atoms in which it can be accurate for the exchange and correlation energies separately, and not just their sum as in bonded systems.

SCAN performs well in:
* atomization energies
* lattice constants of solids
* Short range weak interactions (hydrogen-bonds and vdW interactions for closed shell molecules)
 * No semilocal functional can capture long-range vdW interactions (need correction)

SCAN performs better than PBEsol and PBE for the reactions tested (ref 5 - Shows the benchmark database-Barrier Heights for Heavy Atom Transfer, Nucleophilic Substitution, Association, and Unimolecular Reactions - hydrogen and non-hydrogen transfer **gas-phase** reactions)

From ref. 7, SCAN is proposed to work better than PBE for defects in semiconductors, surface properties of metals, formation energies and structural phase transitions in semiconductors. Good at predicting band gap.

Typically a much lower computational cost than Hybrid functionals.

**Limitations**

* no SCAN-specific pseudopotentials are available for use in VASP

**Regularized SCAN functional**

From ref.  8, proposed modifications to functional form to eliminate numerical instabilities.

HSE - Heyd-Scuseria-Ernzerhof
----------

RPA - Random Phase Approximation
----------

BEEF-vdw 
----------



References
--------

#. https://youtu.be/Ey00F_vsIiY (Benchmarking DFT and beyond-DFT methods for thermodynamics and electronic properties - Geoffroy Hautier)

#. General Performance of Density Functionals Sérgio Filipe Sousa, Pedro Alexandrino Fernandes, and Maria João Ramos The Journal of Physical Chemistry A 2007 111 (42), 10439-10452 DOI: 10.1021/jp0734474

#. https://youtu.be/03Y0v4Ys3_A (SCAN meta-GGA: predictive power of 17 constraints)

#. Strongly Constrained and Appropriately Normed Semilocal Density Functional. Jianwei Sun, Adrienn Ruzsinszky, and John P. Perdew. Phys. Rev. Lett. 115, 036402 – Published 14 July 2015

#. Benchmark Database of Barrier Heights for Heavy Atom Transfer, Nucleophilic Substitution, Association, and Unimolecular Reactions and Its Use to Test Theoretical Methods. Yan Zhao, Núria González-García, and Donald G. Truhlar. The Journal of Physical Chemistry A 2005 109 (9), 2012-2018. DOI: 10.1021/jp045141s

#. Accuracy of Density Functional Theory for Predicting Kinetics of Methanol Synthesis from CO and CO2 Hydrogenation on Copper. Maliheh Shaban Tameh, Albert K. Dearden, and Chen Huang. The Journal of Physical Chemistry C 2018 122 (31), 17942-17953. DOI: 10.1021/acs.jpcc.8b06498

#. https://templeefrc.org/scan-overview

#. Albert P. Bartók and Jonathan R. Yates , "Regularized SCAN functional", J. Chem. Phys. 150, 161101 (2019) https://doi.org/10.1063/1.5094646
