#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#SBATCH -p high
#SBATCH --job-name=opt_try
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=8:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SiBATCH --exclusive

"""
Created on Thu Mar 26 17:10:56 2020

@author: ark245
"""
import os, sys 
sys.path.insert(0,'/home/tdprice/tests/kultools/')
from ase import io
from kul_tools import KulTools as KT
import numpy as np

#what is gamma_only
#
kt = KT(gamma_only=False,structure_type='metal')
kt.set_calculation_type('opt')
atoms = io.read('manual_start.traj')
atoms.pbc=True
kt.set_structure(atoms)

TE = []
KPTS = [1, 2, 3, 4, 5, 6, 7, 8]

for k in KPTS:
    kt.set_overall_vasp_params({'gga':'RP' , 'ivdw': 0, 'encut': 300, 'kpts':(k,k,k)},'isif':3)
    atoms = kt.run()
    atoms = io.read('opt' + '_' +  str(300) + '_' + str(k) + str(k) + str(k) + '/CONTCAR') 
#    TE.append(atoms.get_potential_energy())
    atoms.pbc=True
    kt.set_structure(atoms)

#import matplotlib.pyplot as plt

# consider the change in energy from lowest energy state
#TE = np.array(TE)
#TE -= TE.min()

#plt.plot(KPTS, TE)
#plt.xlabel('number of k-points in each dimension')
#plt.ylabel('Total Energy (eV)')
#plt.savefig('MgO-kpt-convergence.png')
#print(kt.calc_default.int_params['ismear'])
#print(kt.calc_default.special_params['lreal'])
#print(kt.calculation_type)


# Calculation type 
# opt --> needs atoms 
# opt_fine --> needs constraints 
# vib --> needs constraints 
# dimer --> needs path annd atoms 
# neb --> needs traj 

