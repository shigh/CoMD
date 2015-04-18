#!/bin/sh
#PBS -l nodes=4:ppn=32:xe
#PBS -l walltime=00:20:00
#PBS -N mpi-strongscaling

TD='--temp 0 --delta 0'
N=16
X=160

# Simple strong scaling study with eam potential and 256,000 atoms
# aprun -n 1  ../bin/CoMD-mpi -e -i 1 -j 1 -k 1 -x 40 -y 40 -z 40
aprun -n 1 ../bin/CoMD-mpi -e -i 1 -j 1 -k 1 -x $X -y $X -z $X $TD
aprun -n 8 ../bin/CoMD-mpi -e -i 2 -j 2 -k 2 -x $X -y $X -z $X $TD
aprun -N $N -n 64 ../bin/CoMD-mpi -e -i 4 -j 4 -k 4 -x $X -y $X -z $X $TD
