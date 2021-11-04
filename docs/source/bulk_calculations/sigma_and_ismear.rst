SIGMA and ISMEAR
===========

Overview
--------

From Sholl book:

In a metal the Brillouin zone can be divided into regions that are occupied and unoccupied by electrons. The surface in k-space that separates these two regions is called the Fermi surface. Leads to difficulty in calculations because the functions that are integrated change discontinuously from nonzero values to zero at the Fermi surface. If no special efforts are made in calculating these integrals, very large numbers of k points are needed to get well-converged results. 

From Kitchin book:

"In the self-consistent cycle of a DFT calculation, the total energy is minimized with respect to occupation of the Kohn-Sham orbitals. At absolute zero, a band is either occupied or empty. This discrete occupation results in discontinuous changes in energy with changes in occupation, which makes it difficult to converge. One solution is to artificially broaden the band occupancies, as if they were occupied at a higher temperature where partial occupation is possible. This results in a continuous dependence of energy on the partial occupancy, and dramatically increases the rate of convergence. SIGMA and ISMEAR affect how the partial occupancies of the bands are determined.

Some rules to keep in mind:

The smearing methods were designed for metals. For molecules, semiconductors and insulators you should use a very small SIGMA (e.g. 0.01).
Standard values for metallic systems is SIGMA=0.1, but the best SIGMA may be material specific.
The consequence of this finite temperature is that additional bands must be included in the calculation to allow for the partially occupied states above the Fermi level; the number of extra bands depends on the temperature used. An example of the maximum occupancies of the bands for an Cu bulk as a function of SIGMA is shown in Figure fig:sigma-occ. Obviously, as SIGMA approaches 0, the occupancy approaches a step function. It is preferable that the occupancy of several of the highest bands be zero (or at least of order 1×10−8) to ensure enough variational freedom was available in the calculation. Consequently, it is suggested that fifteen to twenty extra bands be used for a SIGMA of 0.20. In any case, it should be determined that enough bands were used by examination of the occupancies. It is undesirable to have too many extra bands, as this will add computational time." 



Effect of SIGMA and ISMEAR
-----------------
The following values were used as a default for a metallic system for the k-pt convergence testing: sigma=0.2,ismear=1.


Computational Expense
------

| 0.001 did not converge
| 0.05/opt_300_444/OUTCAR:                         Elapsed time (sec):    18432.327
| 0.1/opt_300_444/OUTCAR:                         Elapsed time (sec):     1233.967
| 0.2/opt_300_444/OUTCAR:                         Elapsed time (sec):     1255.606
| 0.5/opt_300_444/OUTCAR:                         Elapsed time (sec):     1374.226

