""" This is the script for setting up the env for GPAW on Sherlock"""
# Add modules (dependent on computer)
#module add py-scipy/0.17.0 py-numpy/1.10.4 openmpi/1.8.7/gcc openblas/0.2.15 hdf5/1.8.16  # gcc
module add py-scipy/0.17.0 py-numpy/1.10.4 hdf5/1.8.16 intel/2016.u1 openmpi/1.10.2/intel  #Intel
# load openmpi last otherwise you get intelmpi compiler!

# Define paths for each program (this needs to changed for each computer)
# For intel:
#MKL_path=/share/sw/non-free/intel/2016/u1/mkl/lib/intel64
MKL_path=${MKLROOT}/lib/intel64 
PROGRAM_PATH=${HOME}/programs
ASE_PATH=${PROGRAM_PATH}/ase
GPAW_HOME=${PROGRAM_PATH}/gpaw
#FFTW_PATH=${PROGRAM_PATH}/fftw-3.3.4/install
LIBXC_PATH=${PROGRAM_PATH}/libxc-trunk/install
LIBVDWXC_PATH=${PROGRAM_PATH}/libvdwxc_compiled
FFTW3_PATH=${PROGRAM_PATH}/fftw-3.3.5/build
#LAPACK_PATH=${PROGRAM_PATH}/lapack-3.6.0  # /install?
LAPACK_PATH=${MKL_PATH}
#SCALAPACK_PATH=${PROGRAM_PATH}/scalapack-2.0.2/install
SCALAPACK_PATH=${MKL_PATH}

# Set the paths (this should be the same on all computers
# Set paths for FFTW
# export PATH=${FFTW_PATH}/bin:$PATH
# export LD_LIBRARY_PATH=${FFTW_PATH}/lib:${LD_LIBRARY_PATH}
# export LIBRARY_PATH=${FFTW_PATH}/lib:${LIBRARY_PATH}
# export CPATH=${FFTW_PATH}/include:${CPATH}
# export MANPATH=${FFTW_PATH}/share/man:${MANPATH}

# Set paths for LibXC
export PATH=${LIBXC_PATH}/bin:$PATH
export LD_LIBRARY_PATH=${LIBXC_PATH}/lib:${LD_LIBRARY_PATH}
export LIBRARY_PATH=${LIBXC_PATH}/lib:${LIBRARY_PATH}
export CPATH=${LIBXC_PATH}/include:${CPATH}

# Set paths for libvdwxc
export PATH=${LIBVDWXC_PATH}/bin:$PATH
export LD_LIBRARY_PATH=${LIBVDWXC_PATH}/lib:${LD_LIBRARY_PATH}
export LIBRARY_PATH=${LIBVDWXC_PATH}/lib:${LIBRARY_PATH}
export CPATH=${LIBVDWXC_PATH}/include:${CPATH}

# Set paths for FFTW3
export PATH=$PATH:${FFTW3_PATH}/bin
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${FFTW3_PATH}/lib
export LIBRARY_PATH=${LIBRARY_PATH}:${FFTW3_PATH}/lib
export CPATH=${CPATH}:${FFTW3_PATH}/include

# Set paths for SCALAPACK
export SCALAPACK=${SCALAPACK_PATH}  #/libscalapack.a
export LD_LIBRARY_PATH=${SCALAPACK_PATH}/lib:${LD_LIBRARY_PATH}
export LIBRARY_PATH=${SCALAPACK_PATH}/lib:${LIBRARY_PATH}

# Set paths for LAPACK
export PATH=${LAPACK_PATH}/bin:$PATH
export LD_LIBRARY_PATH=${LAPACK_PATH}/lib:${LD_LIBRARY_PATH}
export LIBRARY_PATH=${LAPACK_PATH}/lib:${LIBRARY_PATH}
export CPATH=${LAPACK_PATH}/include:${CPATH}

# Set paths for ASE
export PYTHONPATH=${ASE_PATH}:$PYTHONPATH
export PATH=${ASE_PATH}/tools:$PATH

# Set paths for GPAW
export GPAW_PLATFORM=`python -c "from distutils import util, sysconfig; print util.get_platform()+'-'+sysconfig.get_python_version()"`
export PYTHONPATH=${GPAW_HOME}:${PYTHONPATH}
export PYTHONPATH=${GPAW_HOME}/build/lib.${GPAW_PLATFORM}:${PYTHONPATH}
export PATH=${GPAW_HOME}/build/bin.${GPAW_PLATFORM}:${GPAW_HOME}/tools:${PATH}
# define path for setups
# 0.9.2000 setups
export GPAW_SETUP_PATH=${HOME}/paw_pseudos/gpaw_setups_ind:${HOME}/paw_pseudos/gpaw-setups-0.9.20000
# 0.8 setups
#export GPAW_SETUP_PATH=${HOME}/paw_pseudos/gpaw_setups_ind:${HOME}/paw_pseudos/gpaw-setups-0.8.7929

# Set OMP and MKL flags
# never thread!
export MKL_NUM_THREADS=1
export OMP_NUM_THREADS=1

# Set paths for /usr/lib and /usr/lib64 to get matplotlib to work
export PYTHONPATH=${PYTHONPATH}:/usr/lib/python2.6/site-packages:/usr/lib64/python2.6/site-packages
