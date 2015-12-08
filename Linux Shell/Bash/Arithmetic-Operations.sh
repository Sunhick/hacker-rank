!#/bin/bash

read X

printf "%.3f" $(echo "$X" | bc -l)
