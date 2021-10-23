import os, sys
from ase import io
import matplotlib.pyplot as plt
import numpy as np

encut = [300, 350, 400, 450, 500, 550]
TE = []

for e in encut:
    atoms = io.read('../../Desktop/pt_mgo/Pt-MgO/data/encut_convergence/opt' + '_' +  str(e) + '_' + '444' + '/vasprun.xml',':')
    print(e, "encut-value")
    print(atoms[-1].get_potential_energy())
    TE.append(atoms[-1].get_potential_energy())


# consider the change in energy from lowest energy state
TE = np.array(TE)
TE -= TE.min()

plt.plot(encut, TE)
plt.xlabel('Energy Cutoff')
plt.ylabel('Total Energy relative to lowest energy structure (eV)')
plt.savefig('MgO-Encut-convergence.png')