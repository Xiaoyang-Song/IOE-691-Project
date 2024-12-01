#!/bin/bash
# Generate tree instances

# Some examples
# python BinaryTreeGenerator.py -n 20 --min 5 --max 10 -o balanced/20.txt
# python BinaryTreeGenerator.py -n 50 --min 0 --max 1 -o balanced/50.txt -b
# python BinaryTreeGenerator.py -n 100 --min 5 --max 10 -o balanced/100.txt
# python BinaryTreeGenerator.py -n 200 --min 5 --max 10 -o balanced/200.txt

# python BinaryTreeGenerator.py -n 50 --min 0 --max 1 -b -o imbalanced/50.txt
# python BinaryTreeGenerator.py -n 200 --min 5 --max 10 -o imbalanced/200.txt
# python BinaryTreeGenerator.py -n 100 --min 5 --max 10 -o imbalanced/100.txt

# Generate multiple randomized instances
n=50
out="balanced/$n"
mkdir -p "source/balanced/$n"
for i in {1..100}
do
    python BinaryTreeGenerator.py -n "$n" --min 0 --max 1 -o "$out/$i.txt" -b
done