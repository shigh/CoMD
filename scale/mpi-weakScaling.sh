#!/bin/sh
#PBS -l nodes=256:ppn=32:xe
#PBS -l walltime=00:20:00
#PBS -N mpi-weakscaling

TD='--temp 600 --delta 0'
N=16

cd ${PBS_O_WORKDIR}

# Simple weak scaling study with eam potential and 32000 atoms per task
aprun -n 1  ../bin/CoMD-mpi -e -i 1 -j 1 -k 1 -x 20 -y 20 -z 20 $TD
aprun -n 8  ../bin/CoMD-mpi -e -i 2 -j 2 -k 2 -x 40 -y 40 -z 40 $TD
aprun -N $N -n 64 ../bin/CoMD-mpi -e -i 4 -j 4 -k 4 -x 80 -y 80 -z 80 $TD
aprun -N $N -n 512 ../bin/CoMD-mpi -e -i 8 -j 8 -k 8 -x 160 -y 160 -z 160 $TD
aprun -N $N -n 4096 ../bin/CoMD-mpi -e -i 16 -j 16 -k 16 -x 320 -y 320 -z 320 $TD
