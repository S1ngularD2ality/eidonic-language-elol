# Eidonic Agent Initiator — Roadmap

*Status: active build • Target stack: Windows 11 + WSL2 (Ubuntu) • GPU: RTX 3060 12GB • Local LLM host: Ollama • Containers: ECP (no Docker in final), dev fallback: venv*

---

## 0) North Star
**EAI** becomes a **model-assisted agent foundry** that can:
- Scaffold, verify, and containerize any agent (CLI-first, optional GUI later).
- Learn from your corpus (Teacher_Protocol_001) via **RAG** + **QLoRA adapters**.
- Emit **ECP** containers (self-describing, reproducible, offline-friendly) for agents & swarms.
- Seed **EidonCore EKRP** embodiments and **RTS game agents**.

---

## 1) Pillars
1. **Data Forge (Teacher_Protocol_001)** – Curate, summarize, and index mixed corpora; export SFT datasets.
2. **Foundry (EAI)** – Wizard + templates → opinionated, secure agent skeletons; codegen + tests.
3. **Memory (RAG)** – Local retrieval layer (TF‑IDF baseline → SBERT/Ollama upgrades).
4. **Learning (QLoRA)** – Fine-tune adapters for an *Agent Planner* model (`eai-teacher`).
5. **Run & Observe** – ECP runtime; health, doctor, audit logs, SBOM.
6. **Security-by-Design** – Policy gates, tool allowlists, network/FS guards, red-team checks.

---

## 2) Current Baseline
- **Teacher_Protocol_001** running with time‑boxed curation, streaming write, subdir recursion.
- **Indexing**: TF‑IDF backend (offline) → `teacher_index.joblib`.
- **RAG planning**: `coach-rag` (retrieval + local generation via Ollama `llama3`).
- **SFT export**: Alpaca JSONL for QLoRA training.

Paths we standardize:
```
[EAI ROOT]          C:\Eidon\eidonic_agent_initiator\
[Teacher agent]     C:\Eidon\eidonic_agent_initiator\Teacher_Protocol_001\
[Convos in]         C:\Eidon\convos\
[Curated out]       C:\Eidon\teacher_out\
[Index out]         C:\Eidon\eidonic_agent_initiator\Teacher_Protocol_001\data\index\teacher_index.joblib
[SFT out]           C:\Eidon\eidonic_agent_initiator\Teacher_Protocol_001\datasets\eai_teacher_sft.jsonl
```

---

## 3) Near-Term Milestones (M-series)

### M0.3 → **Reliable RAG & Time-Boxed Curation** *(DONE / polishing)*
- ✅ Streaming curator with `--max-hours` and per-file progress.
- ✅ TF‑IDF indexer (offline) + CLI hardened (`--from-dir`, `--pattern`).
- ⬜ SBERT backend (online) re‑enable when HF reachable.
- ⬜ Ollama embeddings backend after updating to `/api/embeddings` build.

### M0.4 → **Adapter Training Loop**
- ⬜ WSL2 training rig (LLaMA‑Factory), QLoRA on `mistral-7b-instruct`.
- ⬜ Produce `adapters/eai-teacher-lora/` + **Modelfile** → `ollama create eai-teacher`.
- ⬜ EAI wizard `--ai --model eai-teacher` path hardened; test with 3 briefs.

### M0.5 → **Agent QA & ECP Packaging**
- ⬜ Golden template pack: python-agent, toolrunner, crawler, evaluator.
- ⬜ Built-in test harness (unit + smoke + policy checks) per template.
- ⬜ ECP container spec v0.2 (manifest, policy, sbom, start hooks, doctor).

### M0.6 → **GUI (thin), Profiles, & Publishing**
- ⬜ Minimal Electron/React shell for wizard, logs, doctor.
- ⬜ One-click package to `.eidon` and share.

### M0.7 → **Swarm Patterns & Orchestrator**
- ⬜ EAI emits N‑agent swarms with shared memory + task graph runner.
- ⬜ “Swarm Lord” prototype (orchestration, routing, health, rollback).

---

## 4) Daily Ops — Canonical Commands
**Run from** `C:\Eidon\eidonic_agent_initiator\Teacher_Protocol_001`.

### Curate (6‑hour epoch)
```powershell
python -m agent.main curate --src "C:\Eidon\convos" --out-dir "C:\Eidon\teacher_out" `
  --epochs 999999 --streams 2 --csv-rows 300 --parquet-rows 300 `
  --max-chars 2000 --overlap 150 --max-tokens 220 --max-hours 6
```

### Build Index (offline TF‑IDF)
```powershell
python -m agent.main index-build --from-dir "C:\Eidon\teacher_out" `
  --pattern "curated-*.jsonl" --out .\data\index\teacher_index.joblib `
  --embed-backend tfidf
```

### Plan with RAG
```powershell
python -m agent.main coach-rag "RTS agent that scouts, avoids patrols, and updates a heatmap." `
  --index .\data\index\teacher_index.joblib --k 6 `
  --embed-backend tfidf --model llama3
```

### Export SFT for Training
```powershell
python -m agent.main export-sft --from-dir "C:\Eidon\teacher_out" `
  --pattern "curated-*.jsonl" --out .\datasets\eai_teacher_sft.jsonl
```

---

## 5) Training Track (Adapters → `eai-teacher`)

### 5.1 WSL2 Setup (once)
- Install Ubuntu via Microsoft Store, enable WSL2.
- Inside WSL2:
```bash
python3 -m venv ~/.venvs/eai-train && source ~/.venvs/eai-train/bin/activate
pip install --upgrade pip
pip install llama-factory[torch,metrics] bitsandbytes
```

### 5.2 Move dataset
Copy `eai_teacher_sft.jsonl` to WSL: `~/data/eai_teacher_sft.jsonl`.

### 5.3 Train (QLoRA config)
```bash
llamafactory-cli train \
  --model_name_or_path mistralai/Mistral-7B-Instruct-v0.3 \
  --finetuning_type lora --dataset_format alpaca \
  --train_file ~/data/eai_teacher_sft.jsonl \
  --output_dir ~/adapters/eai-teacher-lora \
  --bf16 True --do_train \
  --per_device_train_batch_size 1 --gradient_accumulation_steps 8 \
  --learning_rate 1e-4 --num_train_epochs 2 --lr_scheduler_type cosine \
  --logging_steps 20 --save_steps 200 --save_total_limit 2 \
  --max_source_length 1024 --max_target_length 512 \
  --lora_r 16 --lora_alpha 32 --lora_dropout 0.05 \
  --load_in_4bit True --bnb_4bit_quant_type nf4 --bnb_4bit_use_double_quant True
```

### 5.4 Load adapter in Ollama (Windows)
- Copy `~/adapters/eai-teacher-lora` → `C:\Eidon\ollama_adapters\eai-teacher-lora\`
- Create **Modelfile** `C:\Eidon\ollama_adapters\Modelfile.eai-teacher`:
```
FROM mistral:7b-instruct
ADAPTER C:\Eidon\ollama_adapters\eai-teacher-lora
TEMPLATE """{{ .System }}\n\nUser: {{ .Prompt }}\n\nAssistant:"""
SYSTEM """You are the Eidonic Agent Planner. Output compact JSON: {name, description, tools[], recipe[], notes[]}.
Minimize prose. Enforce safety and correctness."""
```
- Build model: `ollama create eai-teacher -f C:\Eidon\ollama_adapters\Modelfile.eai-teacher`

### 5.5 Use it in EAI wizard
```powershell
cd C:\Eidon\eidonic_agent_initiator
python -m eai.cli wizard --preview --ai --model eai-teacher --brief "Create a containerized map-analyzer agent with fs.find, regex.scan, and job runner."
```

---

## 6) ECP (Eidonic Container Protocol) — v0.2 Draft
**Goals:** Docker‑free portability, offline reproducibility, minimal overhead.

**Container Layout (.eidon):**
```
agent/                 # code
  main.py
  runtime/*
config/
  policy.yml           # tool allowlist, FS/HTTP guards
  limits.yml           # rate/time/memory caps
manifest.yml           # name, version, entrypoints, requirements, health
sbom.json              # generated (pip freeze + hashes)
logs/
  run/*                # stdout/stderr, audits
```

**Runtime hooks:**
- `eidon run <container>.eidon [cmd]` → venv bootstrap → policy mount → launch entrypoint.
- `eidon doctor` → verify policy, limits, deps; emit SBOM + report.
- `eidon pack` → build archive from working agent dir.

**Hardening:**
- FS roots allowlist; network `allow_domains`; tool RBAC.
- Repro lockfile for Python deps (hash‑pinned requirements).

---

## 7) Security & Quality Gates
- **Policy**: default‑deny tools; opt‑in allowlist per agent.
- **Static**: ruff/flake8 + bandit on templates.
- **Runtime**: timeouts, max tokens, FS/network guards.
- **Tests**: harness per template (unit + smoke + red‑team prompts).

---

## 8) ARC Solver Swarm (preview topology)
1) **Task Planner** (model‑guided) – decomposes ARC instance to subproblems.
2) **Perceptual Mapper** – converts grid to symbols (colors, shapes, relations).
3) **Program Synthesizer** – proposes DSL steps (transformations).
4) **Verifier/Executor** – runs candidate programs on examples.
5) **Searcher** – guided search over program space (beam/MCTS hybrid).
6) **Hypothesis Memory** – caches transformations & scores.
7) **Constraint Critic** – prunes via invariants/constraints.
8) **Curriculum Teacher** – auto‑generates/evaluates teaching tasks for weak spots.
9) **Explainer** – renders solution trace (for eval + human trust).
10) **Orchestrator** – budgets, retries, data plumbs; halting policy.

*Interfaces:* JSON task graph; shared key-value memory; small visual DSL; pluggable LLM(s). EAI emits each agent via template + policy + tests; Teacher curates ARC corpus → SFT adapters for planner/synth.

---

## 9) Risks & Mitigations
- **Thermals/VRAM**: use `--streams 1–2`, 4‑bit QLoRA, power cap −10% if >85°C.
- **Offline limits**: TF‑IDF backend ensures RAG always works; add SBERT when online.
- **Drift**: pin templates + policy versions in manifest; use `doctor` before pack.
- **Path drift**: single canonical OUT = `C:\Eidon\teacher_out`.

---

## 10) Definition of Done (phase)
- M0.4: `eai-teacher` adapter produces measurably better wizard plans vs. base.
- M0.5: agents pack into `.eidon`, pass doctor, run offline.
- M0.6: minimal GUI drives wizard + doctor; publishable demo agents.
- M0.7: Swarm Lord prototype orchestrates ≥3 cooperating agents on a toy task.

---

## 11) Quick Checklists
**Before curate:** Ollama running; `C:\Eidon\convos` has files.  
**After curate:** JSONL exists in `C:\Eidon\teacher_out`.  
**Before index:** `teacher_index.joblib` regenerates without errors.  
**Before SFT:** dataset non‑empty; spot‑check a few lines.  
**Before training:** WSL2 venv ok, disk headroom > 10 GB.  
**Before pack:** `doctor` passes; policy/limits pinned.

---

## 12) Next Actions (you & me)
1) Let the 6‑hour curation finish; then run **index-build**, **coach-rag**, **export-sft**.
2) Green‑light **M0.4**: I’ll prepare a LLaMA‑Factory YAML tuned for 12GB.
3) Ship **ECP v0.2** pack/doctor skeletons into the templates.
4) Start ARC swarm scaffolds (10 micro‑agents + task graph, minimal DSL).

*We move in phases; the mirror holds the pattern. When you’re ready, say “drop the M0.4 train.yaml,” and I’ll place it.*

