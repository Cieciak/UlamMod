#! /bin/bash

for ((n = 2; n <= 6; n++))
do
  for ((i = 1; i < n; i++))
  do
    python3.10 init.py $n*n+$i ./svg/$n*n+$i.svg
  done  
done