# Precision as a Dynamic Training Resource

[![Kaggle](https://img.shields.io/badge/run-Kaggle-20BEFF?logo=kaggle)](https://www.kaggle.com/code/boxyml/precision-as-dynamic-training)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21571029.svg)](https://doi.org/10.5281/zenodo.21571029)
[![License: MIT](https://img.shields.io/badge/code-MIT-green.svg)](LICENSE)
![Python Versions](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-3776AB?logo=python&logoColor=white)
![Tests](https://github.com/AdamBoxy/precision-as-dynamic-training/actions/workflows/tests.yml/badge.svg)

> **Research status:** exploratory hypothesis and reproducible proof of concept. This repository does **not** claim a new state-of-the-art algorithm, production-ready low-precision kernels, or measured hardware savings.

## Research question

Can numerical precision be treated as a dynamic training resource and allocated according to current learning activity?

This project introduces **Learning-Activity Precision Allocation (LAPA)**, a small controller that observes a training signal and assigns simulated precision levels during optimization.

## Reported proof-of-concept results

| Regime | Validation accuracy | Effective precision |
|---|---:|---:|
| FP32 baseline | 96.07% | 32 bits |
| Static 8-bit | 96.67% | 8 bits |
| Adaptive LAPA | 96.37% | ~5.28 bits |
| Static 4-bit | 38.89% | 4 bits |

These results support a narrow claim: adaptive allocation preserved behavior that uniform aggressive quantization destroyed in this experiment. They do not establish end-to-end speed, energy, memory, or hardware advantages.

## Repository structure

```text
├── src/lapa/              # controller and fake quantization
├── experiments/           # runnable synthetic demonstration
├── tests/                 # unit tests
├── results/               # published summary and generated outputs
├── docs/                  # methodology, limitations, context, roadmap
├── notebooks/             # canonical Kaggle notebook reference
└── .github/workflows/     # CI
```

## Quick start

```bash
python -m venv .venv
pip install -e .[dev]
pytest
python experiments/run_proof_of_concept.py
```

The included experiment uses synthetic data as a repository smoke test. The canonical published notebook contains the full narrative experiment.

## Core design

1. Observe a learning-activity signal.
2. Map that signal to a permitted bit width.
3. Track the average assigned precision as a budget proxy.
4. Compare model quality against fixed-precision baselines.

The current implementation uses deterministic fake quantization. Values remain floating point while quantization error is simulated numerically.

## Scope

This repository demonstrates a testable controller abstraction, reproducible simulated quantization, fixed-precision baselines, effective-bit accounting, and a path toward systems evaluation.

It does not yet demonstrate native low-bit kernels, reduced wall-clock time, reduced device memory, lower energy use, transformer-scale behavior, or superiority over the broader adaptive-precision literature.

See [`docs/limitations.md`](docs/limitations.md).

## Research links

- [Zenodo record](https://zenodo.org/records/21571029)
- DOI: [`10.5281/zenodo.21571029`](https://doi.org/10.5281/zenodo.21571029)

## Reproducibility philosophy

- Make the hypothesis falsifiable.
- Distinguish simulation from hardware evidence.
- Preserve unsuccessful baselines.
- Report effective precision beside model quality.
- Invite replication and critique.
- Change claims when evidence changes.

## License and citation

Code and repository documentation are released under the [MIT License](LICENSE). Cite the archived Zenodo record or use GitHub's **Cite this repository** menu generated from [`CITATION.cff`](CITATION.cff).

---

**BoxyML Research · BXR-2026-001 · v0.1.0**
