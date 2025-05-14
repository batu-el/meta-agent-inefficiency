#!/bin/bash

benchmarks=("_mmlu" "_mgsm" "_drop" "_gpqa")

script="search_parallel.py"

for bench in "${benchmarks[@]}"; do
  echo "Launching $bench/$script --expr_name run3 in background..."
  python "$bench/$script" --expr_name run3 &
done

wait
echo "All runs completed."