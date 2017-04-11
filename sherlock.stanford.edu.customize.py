""" This is the customize script for GPAW on Sherlock"""
"""User provided customizations.

Here one changes the default arguments for compiling _gpaw.so (serial)
and gpaw-python (parallel).

Here are all the lists that can be modified:
    
* libraries
* library_dirs
* include_dirs
* extra_link_args
* extra_compile_args
* runtime_library_dirs
* extra_objects
* define_macros
* mpi_libraries
* mpi_library_dirs
* mpi_include_dirs
* mpi_runtime_library_dirs
* mpi_define_macros

To override use the form:
    
    libraries = ['somelib', 'otherlib']

To append use the form

    libraries += ['somelib', 'otherlib']
"""

#careful here:
# mpiicc is intelmpi wrapper for icc
# mpicc is openmpi wrapper for a c-compiler (which one?)
# at least with compiler = 'icc', mpicompiler = 'mpicc', mpilinker = 'mpicc'
# icc is used as compiler.
compiler = 'icc -mkl=sequential'
mpicompiler = 'mpicc -mkl=sequential'  # use None if you don't want to build a gpaw-python
mpilinker = 'mpicc -mkl=sequential'
# platform_id = ''
scalapack = True
hdf5 = False

scalapack_dir = '$MKLROOT'
hdf5_dir = '/share/sw/free/hdf5/1.8.16/intel'
libxc_dir = '/home/rasmusk/programs/libxc-3.0.0/install'
libvdwxc_path = '/home/rasmusk/programs/libvdwxc_compiled'

# MKL

library_dirs = ['${MKLROOT}/lib/intel64']#, '${MPI_ROOT}/lib']

# MKL needs to be linked explicitly
libraries = ['mkl_intel_lp64',
             'mkl_core',
             'mkl_sequential',
             'm',
             'dl',
             'pthread',
             'open-rte', # We need these next four because intel IPO needs them defined explicitly
             'open-pal',
             'pmi2',
             'pciaccess']


extra_compile_args = ['-Wall',
                      '-O3',
                      #'-Ofast', # O3 plus more, disregards strict standards compliance
                      #'-O2',
                      '-ipo0',
                      '-fPIC',
                      '-std=c99']

include_dirs += ['${MKLROOT}/include/']#, '${MPI_ROOT}/include']

if hdf5:
    library_dirs += [hdf5_dir + '/lib']
    include_dirs += [hdf5_dir + '/include']

# Use ScaLAPACK:
# Warning! At least scalapack 2.0.1 is required!
# See https://trac.fysik.dtu.dk/projects/gpaw/ticket/230
if scalapack:
    # This actually works!
    # To test it, go to a compute node and run
    # gpaw-python $(which gpaw) info
    # gpaw command cannot show scalapack, only parallel version of
    # gpaw (=gpaw-python) can!
    libraries += ['mkl_scalapack_lp64',
                  'mkl_blacs_openmpi_lp64']
    #library_dirs += ['$MPI_ROOT/lib']
    #extra_link_args += [#scalapack_dir + '/lib/intel64/libmkl_scalapack_lp64.a',
    #                    scalapack_dir + '/lib/intel64/libmkl_blacs_openmpi_lp64.a']
    define_macros += [('GPAW_NO_UNDERSCORE_CBLACS', '1')]
    define_macros += [('GPAW_NO_UNDERSCORE_CSCALAPACK', '1')]

# LibXC:
# In order to link libxc installed in a non-standard location
# (e.g.: configure --prefix=/home/user/libxc-2.0.1-1), use:

# - static linking:
if 0:
    include_dirs += ['/home//include']
    extra_link_args += ['/home/user/libxc-2.0.1-1/lib/libxc.a']
    if 'xc' in libraries:
        libraries.remove('xc')
        
# - dynamic linking (requires rpath or setting LD_LIBRARY_PATH at runtime):
if 1:
    include_dirs += [libxc_dir + '/include']
    library_dirs += [libxc_dir + '/lib']
    # You can use rpath to avoid changing LD_LIBRARY_PATH:
    # extra_link_args += ['-Wl,-rpath=/home/user/libxc-2.0.1-1/lib']
    if 'xc' not in libraries:
        libraries.append('xc')

# libvdwxc:
if 1:
    libvdwxc = True
    #extra_link_args += ['-Wl,-rpath=%s/lib' % libvdwxc_path]
    library_dirs += ['%s/lib' % libvdwxc_path]
    include_dirs += ['%s/include' % libvdwxc_path]
    libraries += ['vdwxc', 'fftw3_mpi', 'fftw3']

# Build MPI-interface into _gpaw.so:
if 0:
    compiler = 'mpicc'
    define_macros += [('PARALLEL', '1')]
    mpicompiler = None

