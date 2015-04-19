#!/bin/sh

:> data_nAtoms.txt
for ((n=10; n<=90; n+=10))
do
    time=`grep -m 1 "force" fLJ_nx${n}_ny${n}_nz${n}.txt | awk '{print $3}'`
    echo "${n} ${time}" >> data_nAtoms.txt
done
