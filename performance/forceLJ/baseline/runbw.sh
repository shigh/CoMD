#!/bin/sh
#PBS -l nodes=1:ppn=1:xe
#PBS -l walltime=01:30:00
#PBS -N fLJ_nAtoms
#PBS -e $PBS_JOBID.err
#PBS -o $PBS_JOBID.out
#PBS -m bea
#PBS -M emolloy2@illinois.edu

cd $PBS_O_WORKDIR

#for ((n=10; n<=100; n+=10))
#do
#    aprun -n 1 ../../bin/CoMD-mpi \
#        --nx ${n} --ny ${n} --nz ${n} \
#        --xproc 1 --yproc 1 --zproc 1 \
#        --nSteps 20 --printRate 5 --dt 1 \
#        --lat 3.615 --temp 0 --delta 0 > fLJ_nx${n}_ny${n}_nz${n}.txt
#done

for n in 250
do
    aprun -n 1 ../../bin/CoMD-mpi \
        --nx ${n} --ny ${n} --nz ${n} \
        --xproc 1 --yproc 1 --zproc 1 \
        --nSteps 3 --printRate 3 --dt 1 \
        --lat 3.615 --temp 0 --delta 0 > fLJ_nx${n}_ny${n}_nz${n}.txt
done
