Functional Benchmarking
============

Overview
-------

what functional to use? 

* Need to balance physical accuracy with computational cost.

* Need to focus on properties of interest.
 * Binding energies
 * Reaction barriers
 * Vibrational frequencies
 * TS geometries
 * Minimum energy geometries

How do we address the physical phenomena that influence performance of real catalyst that are not included in DFT calculations?
Do we need to worry about self-interaction errors? ( hybrid functionals can partially correct for this) 
Does our system have strong electron correlation?

* Known Systems with self-interaction errors
 * actinides
 * various transition-metal oxides that have partially filled d or f shells

Magnesium is a group 2 alkaline earth metal ( electron configuration [Ne] 3s2)

However in MgO, we are interested in the impact of oxygen vacancies and different substitutions of Pt. These systems should be explored for strong electron correlation

Properties - Physical Accuracy
-------

Need to quantify how accurate DFT predictions are for specified property of interest.


B3LYP
-------

SCAN 
----------



References
--------

https://youtu.be/Ey00F_vsIiY (Benchmarking DFT and beyond-DFT methods for thermodynamics and electronic properties - Geoffroy Hautier)

* Things to consider when benchmarking
 * Is data directly comparable to ab initio (temp, pure sample, etc)
 * Is data diverse
 * What are the error bars for experimental measurements?
 * Use several sources to prevent bias
