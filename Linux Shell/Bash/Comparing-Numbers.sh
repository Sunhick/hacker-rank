#!/bin/bash

read X
read Y
if (( X < Y )); then
    echo "X is less than Y"
elif (( X > Y )); then
    echo "X is greater than Y"
elif (( X == Y )); then
    echo "X is equal to Y"
fi

