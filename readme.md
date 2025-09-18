## Meta-Agent Inefficiency

This repository evaluates search and routing strategies for LLM-based meta agents across multiple datasets, tracks compute/token costs.

> Attribution: Dataset implementations and the basis for the agent implementation are adapted from ADAS (Automated Design of Agentic Systems). See: [ShengranHu/ADAS](https://github.com/ShengranHu/ADAS).

### Repository Layout

- `/_drop`, `/_gpqa`, `/_mgsm`, `/_mmlu`: Dataset-specific implementations with mirrored structure:
  - `_cost_tracker.py`: Cost accounting utilities (tokens, API calls, time)
  - `_evaluate.py`: Data loading, running search/routing, computing metrics, saving results
  - `_lm_calls.py`: LLM client wrappers (providers, retries, batching, rate limits)
  - `_routing.py`: Heuristic/static routing among tools/contexts/models
  - `_routing_nn.py`: Nearest neighbor routing
  - `_tracker_context.py`: Per-example decision/context traces and logs
  - `search.py`: Baseline search procedure
  - `search_parallel.py`: Parallelized search variant
  - `search_topk.py`: Top-K (Evolutionary) search variant
  - `utils.py`: Dataset-specific helpers
  - `*_prompt.py`: Prompt templates (e.g., `drop_prompt.py`, `gpqa_prompt.py`)

- `/results`: Saved metrics, traces, and summaries per dataset and search mode
  - `<dataset>/{cumulative,parallel,topk}/*.json(l)`

- `/scripts`: Ready-to-run experiment scripts
  - `run{1,2,3}.sh` (baseline), `run{1,2,3}_parallel.sh`, `run{1,2,3}_topk.sh`

- Root assets: `Figure*.png` snapshots; `requirements.txt` dependencies

### Installation
Environment
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install -U pip
pip install -r requirements.txt
```
Credentials (LLM providers)
- Configure provider credentials as expected by `/_*/_lm_calls.py`.
```bash
export OPENAI_API_KEY=YOUR_KEY   # plus other provider keys if applicable
```

### Running Experiments

Use the provided scripts (for 3 runs); outputs are stored under `/results`.
```bash
# Baseline sequential/cumulative-style runs
bash scripts/run1.sh
bash scripts/run2.sh
bash scripts/run3.sh

# Parallelized search
bash scripts/run1_parallel.sh
bash scripts/run2_parallel.sh
bash scripts/run3_parallel.sh

# Top-K search
bash scripts/run1_topk.sh
bash scripts/run2_topk.sh
bash scripts/run3_topk.sh
```

Outputs:
```
results/
  <dataset>/
    cumulative/   # baseline / cumulative search outputs
    parallel/     # parallel search outputs
    topk/         # top-k search outputs
```
Each subfolder contains dataset-level JSON summaries and per-example JSONL traces including cost logs.

### Key Concepts

- **Search strategies**
  - Baseline: `search.py`
  - Parallel: `search_parallel.py`
  - Top-K: `search_topk.py`
- **Cost tracking**
  - `/_*/_cost_tracker.py`, `/_*/_tracker_context.py`
- **Routing**
  - Heuristic routing: `/_*/_routing.py`
  - Learned routing: `/_*/_routing_nn.py`
- **Prompts**
  - `/*_prompt.py`

### Attribution

- Source for dataset implementations and basis for the agent implementation: [dataset/readme.md](https://github.com/batu-el/meta-agent-inefficiency/blob/main/dataset/readme.md)

### License and Citation

Follow the repository LICENSE if present. If you use this codebase, please cite the project or associated paper. When appropriate, also cite ADAS as the originating implementation reference: [ShengranHu/ADAS](https://github.com/ShengranHu/ADAS)