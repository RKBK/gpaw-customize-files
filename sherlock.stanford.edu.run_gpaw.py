"""This is the submission script for GPAW on Sherlock at Stanford"""
#!/usr/bin/env python
from sys import argv
import os

job = argv[1]
nodes = argv[2]
time = argv[3] + ":00"

if len(argv) > 4:
    gpaw_options = ' '.join(argv[4:])
else:
    gpaw_options = ' '
#options = '-l nodes=' + nodes +':ppn=2' + ' -l' +' walltime=' + time + ' -m abe'
#options = '-N ' + nodes  +' -t ' + time + ' -J ' + job
options = ' -J ' + job 
#dir = os.getcwd() 

f = open('tmp.sh', 'w')

f.write("""\
#!/bin/bash
#SBATCH -n %s
#SBATCH -t %s
#SBATCH -p iric,normal
#SBATCH --exclusive
# Add nodes that always fail
#SBATCH -x gpu-14-1,sh-20-35

# send email about job status changes
##SBATCH --mail-type=ALL

#Set an open-mpi parameter to suppress "fork()" warnings
# GPAW is written to use fork calls
export OMPI_MCA_mpi_warn_on_fork=0

#This next line decides which version of gpaw will be used
source $HOME/environment_scripts/set_paths_gpaw-trunk_scalapack_libvdwxc.sh  # Gpaw trunk with mBEEF-vdW fixed for libvdwxc

srun `which gpaw-python` %s %s
""" % (nodes,time,job,gpaw_options)) 
f.close()

os.system('sbatch ' + options + ' tmp.sh')
