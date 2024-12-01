#!/bin/bash

# Tree instance
instance="source/balanced/50.txt"
out="out/balanced/50"
# D_list=(60 80 100 110 120 130 150 180 200 210 220 230 240 250 300 400)
D_list=(8)

# instance="source/balanced/20.txt"
# out="out/balanced/20"
# D_list=(80 90 100 120 140 160 180 200 220 240 260 280)

# instance="source/balanced/200.txt"
# out="out/balanced/200"
# D_list=(80 90 100 120 140 160 180 200 220 240 260 280)
# out_results="out/balanced/20/results.txt"
# > "$out_results"

mkdir -p "$out"
# Run algo with different D
for D in "${D_list[@]}"
do
    python main.py "$instance" "$D" > "$out/$D.txt"
    # echo $? >> "$out_results"
done
echo "Completed."
