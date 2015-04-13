#!/bin/sh

# Simple strong scaling study with eam potential and 256,000 atoms
aprun -n 1  ../bin/CoMD-mpi -e -i 1 -j 1 -k 1 -x 40 -y 40 -z 40
aprun -n 2  ../bin/CoMD-mpi -e -i 2 -j 1 -k 1 -x 40 -y 40 -z 40
aprun -n 4  ../bin/CoMD-mpi -e -i 2 -j 2 -k 1 -x 40 -y 40 -z 40
aprun -n 8  ../bin/CoMD-mpi -e -i 2 -j 2 -k 2 -x 40 -y 40 -z 40
aprun -n 16 ../bin/CoMD-mpi -e -i 4 -j 2 -k 2 -x 40 -y 40 -z 40
