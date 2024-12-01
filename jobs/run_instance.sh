
# Run on single instances (balanced, 50, 10)
n=50
D=10
instance="source/balanced/50.txt"

out="out/balanced/$n"
mkdir -p "$out"
for i in {1..100}
do
    python main.py "$out/$i.txt" "$D" > "$out/$i.txt"
done