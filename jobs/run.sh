#!/bin/bash

# Tree instance
# instance="source/balanced/50.txt"
# out="out/balanced/50"
# D_list=(200 210 220 230 240 250)

instance="source/balanced/20.txt"
out="out/balanced/20"
D_list=(80 90 100 120 140 160 180 200 220 240 260 280)

mkdir -p "$out"
# Run algo with different D
for D in "${D_list[@]}"
do
    python main.py "$instance" "$D" > "$out/$D.txt"
done
echo "Completed."
