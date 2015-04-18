#!/bin/sh

TD=--temp 0 --delta 0
N=16

# Simple strong scaling study with eam potential and 256,000 atoms
# aprun -n 1  ../bin/CoMD-mpi -e -i 1 -j 1 -k 1 -x 40 -y 40 -z 40
aprun -N $N -n 16 ../bin/CoMD-mpi -e -i 4 -j 2 -k 2 -x 40 -y 40 -z 40 $TD
aprun -N $N -n 32 ../bin/CoMD-mpi -e -i 4 -j 4 -k 2 -x 40 -y 40 -z 40 $TD
aprun -N $N -n 64 ../bin/CoMD-mpi -e -i 4 -j 4 -k 4 -x 40 -y 40 -z 40 $TD
