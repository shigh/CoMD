#!/bin/sh
#PBS -l nodes=256:ppn=32:xe
#PBS -l walltime=01:00:00
#PBS -N mpi-strongscaling

delta='--delta 0'
N=16
X=160

cd ${PBS_O_WORKDIR}

for T in 0 600 3000
do
    TD="--temp ${T} ${delta}"
    aprun -N $N -n 64 ../bin/CoMD-mpi   -i 4 -j 4 -k 4 -x $X -y $X -z $X $TD
    aprun -N $N -n 512 ../bin/CoMD-mpi  -i 8 -j 8 -k 8 -x $X -y $X -z $X $TD
    aprun -N $N -n 4096 ../bin/CoMD-mpi -i 16 -j 16 -k 16 -x $X -y $X -z $X $TD
done
