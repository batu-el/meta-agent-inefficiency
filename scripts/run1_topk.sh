#!/bin/bash

benchmarks=("_mmlu" "_mgsm" "_drop" "_gpqa")

script="search_topk.py"

for bench in "${benchmarks[@]}"; do
  echo "Launching $bench/$script --expr_name run1 in background..."
  python "$bench/$script" --expr_name run1 &
done

wait
echo "All runs completed."