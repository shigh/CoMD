#!/bin/sh

:> data_nAtoms.txt
for n in 10 20 30 40 50 60 70 80 90 100 250
do
    time=`grep -m 1 "force" fLJ_nx${n}_ny${n}_nz${n}.txt | awk '{print $3}'`
    echo "${n} ${time}" >> data_nAtoms.txt
done
