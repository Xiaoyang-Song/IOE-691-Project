#!/bin/bash

# Tree instance
instance="source/balanced/50.txt"
out="out/balanced/50"
mkdir -p "$out"

D_list=(200 210 220 230 240 250)
# Run algo with different D
for D in "${D_list[@]}"
do
    python main.py "$instance" "$D" > "$out/$D.txt"
done
echo "Completed."
