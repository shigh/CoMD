#!/bin/sh

TD='--temp 0 --delta 0'
N=16

# Simple weak scaling study with eam potential and 32000 atoms per task
aprun -N $N -n 1  ../bin/CoMD-mpi -e -i 1 -j 1 -k 1 -x 20 -y 20 -z 20 $TD
aprun -N $N -n 2  ../bin/CoMD-mpi -e -i 2 -j 1 -k 1 -x 40 -y 20 -z 20 $TD
aprun -N $N -n 4  ../bin/CoMD-mpi -e -i 2 -j 2 -k 1 -x 40 -y 40 -z 40 $TD
aprun -N $N -n 8  ../bin/CoMD-mpi -e -i 2 -j 2 -k 2 -x 40 -y 40 -z 40 $TD
aprun -N $N -n 16 ../bin/CoMD-mpi -e -i 4 -j 2 -k 2 -x 80 -y 40 -z 40 $TD
