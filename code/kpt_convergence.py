import os, sys
from ase import io
import matplotlib.pyplot as plt
import numpy as np

KPTS = [1, 2, 3, 4, 5, 6, 7, 8]
TE = []

for k in KPTS:
    atoms = io.read('../../Desktop/pt_mgo/kultools/opt' + '_' +  str(300) + '_' + str(k) + str(k) + str(k) + '/vasprun.xml',':')
    print(k, "k-value")
    print(atoms[-1].get_potential_energy())
    TE.append(atoms[-1].get_potential_energy())


# consider the change in energy from lowest energy state
TE = np.array(TE)
TE -= TE.min()

plt.plot(KPTS, TE)
plt.xlabel('Number of k-points in each dimension')
plt.ylabel('Total Energy relative to lowest energy structure (eV)')
plt.savefig('MgO-kpt-convergence.png')