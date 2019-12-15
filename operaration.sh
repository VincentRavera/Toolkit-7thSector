#!/bin/bash

a=(+ - / )

for i in ${a[@]}
do
    for j in ${a[@]}
    do
        for k in ${a[@]}
        do
            w=$((5 $i 8 $j 6 $k 2))
            echo $w
        done
    done
done
