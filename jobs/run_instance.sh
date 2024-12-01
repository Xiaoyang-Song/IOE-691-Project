
# Run on single instances (balanced, 50, 10)
n=100

D=120
instance="source/balanced/$n"
out="out/balanced/$n-$D"
mkdir -p "$out"

for i in {1..100}
do
    python main.py "$instance/$i.txt" "$D" > "$out/$i.txt"
done

python get.py -mode 'balanced' -n $n -D $D -m 100

instance="source/imbalanced/$n"
out="out/imbalanced/$n-$D"
mkdir -p "$out"
for i in {1..100}
do
    python main.py "$instance/$i.txt" "$D" > "$out/$i.txt"
done

python get.py -mode 'imbalanced' -n $n -D $D -m 100