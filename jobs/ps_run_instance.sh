# Variables
$n = 100
$D = 120

# Run for "balanced" instances
$instance = "source/balanced/$n"
$out = "out/balanced/$n-$D"

# Create the output directory if it doesn't exist
if (-not (Test-Path -Path $out)) {
    New-Item -ItemType Directory -Force -Path $out
}

# Loop through instances and process
for ($i = 1; $i -le 100; $i++) {
    python main.py "$instance/$i.txt" $D | Out-File -FilePath "$out/$i.txt" -Encoding UTF8
}

# Run the summary Python script for "balanced"
python get.py -mode 'balanced' -n $n -D $D -m 100

# Run for "imbalanced" instances
$instance = "source/imbalanced/$n"
$out = "out/imbalanced/$n-$D"

# Create the output directory if it doesn't exist
if (-not (Test-Path -Path $out)) {
    New-Item -ItemType Directory -Force -Path $out
}

# Loop through instances and process
for ($i = 1; $i -le 100; $i++) {
    python main.py "$instance/$i.txt" $D | Out-File -FilePath "$out/$i.txt" -Encoding UTF8
}

# Run the summary Python script for "imbalanced"
python get.py -mode 'imbalanced' -n $n -D $D -m 100
