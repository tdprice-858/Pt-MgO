#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#SBATCH -p high
#SBATCH --job-name=opt_try
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=24:00:00
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
atoms = io.read('0.1/opt_300_444/CONTCAR')
atoms.pbc=True

TE = []
SIGMA = [0.2, 0.5]

for sigma in SIGMA:
    cwd = os.getcwd()
    if not os.path.exists(str(sigma)):
        os.makedirs(str(sigma))
    os.chdir(str(sigma))
    kt = KT(gamma_only=False,structure_type='metal')
    kt.set_calculation_type('opt')
    kt.set_structure(atoms)

    kt.set_overall_vasp_params({'gga':'RP' , 'ivdw': 0, 'encut': 300, 'kpts':(4,4,4),'sigma':sigma})
    atoms = kt.run()
    atoms = io.read('opt' + '_' +  str(300) + '_' + '444' + '/CONTCAR')
#    TE.append(atoms.get_potential_energy())
    atoms.pbc=True
    os.chdir(cwd)

