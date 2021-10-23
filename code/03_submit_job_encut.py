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

import os, sys
sys.path.insert(0,'/home/tdprice/tests/kultools/')
from ase import io
from kul_tools import KulTools as KT
import numpy as np

#what is gamma_only
#
kt = KT(gamma_only=False,structure_type='metal')
kt.set_calculation_type('opt')
atoms = io.read('opt_350_444/CONTCAR')
atoms.pbc=True
kt.set_structure(atoms)

TE = []
encut = [400, 450, 500, 550]

for e in encut:
    kt.set_overall_vasp_params({'gga':'RP' , 'ivdw': 0, 'encut': e, 'kpts':(4,4,4),'isif':2})
    atoms = kt.run()
    atoms = io.read('opt' + '_' +  str(e) + '_' + '444' + '/CONTCAR')
#    TE.append(atoms.get_potential_energy())
    atoms.pbc=True
    kt.set_structure(atoms)
