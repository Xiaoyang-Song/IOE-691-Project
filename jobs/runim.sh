#!/bin/bash

# Tree instance
instance="source/imbalanced/50.txt"
out="out/imbalanced/50"
D_list=(10)

# instance="source/imbalanced/30.txt"
# out="out/imbalanced/30"
# D_list=(60 80 100 110 120 130 150 180 200 210 220 230 240 250 300 400)

# instance="source/imbalanced/100.txt"
# out="out/imbalanced/100"
# D_list=(160)

# instance="source/imbalanced/200.txt"
# out="out/imbalanced/200"
# D_list=(160)


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
