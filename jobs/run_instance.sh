
# Run on single instances (balanced, 50, 10)
n=100

# D=12
# instance="source/balanced/$n"
# out="out/balanced/$n-$D"
# mkdir -p "$out"

# for i in {1..10}
# do
#     python main.py "$instance/$i.txt" "$D" > "$out/$i.txt"
# done

D=15
instance="source/imbalanced/$n"
out="out/imbalanced/$n-$D"
mkdir -p "$out"

for i in {1..10}
do
    python main.py "$instance/$i.txt" "$D" > "$out/$i.txt"
done