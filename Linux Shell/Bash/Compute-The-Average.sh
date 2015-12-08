#!/bin/bash

read X
Z=0
for(( i=1 ; i<=X ; i++))
do
    read Y
    Z=$(echo $Z+$Y| bc)
done

printf "%.3f" $(echo "$Z/$X" | bc -l)

