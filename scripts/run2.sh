#!/bin/bash

benchmarks=("_mmlu" "_mgsm" "_drop" "_gpqa")

script="search.py"

for bench in "${benchmarks[@]}"; do
  echo "Launching $bench/$script --expr_name run2 in background..."
  python "$bench/$script" --expr_name run2 &
done

wait
echo "All runs completed."