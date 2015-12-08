#!/bin/bash

read X
read Y
read Z
read char
if [[ "$X" == "$Y" && "$Y" == "$Z" ]]
then
	echo "EQUILATERAL"
elif [[ "$X" == "$Y" || "$Y" == "$Z" ]]
then
    echo "ISOSCELES"
else
	echo "SCALENE"
fi
