# Contributing

Useful contributions include independent reproductions, failed reproductions with environment details, alternative activity signals, hardware measurements, baseline comparisons, negative results, and documentation corrections.

## Research integrity

Distinguish clearly among simulated precision, storage compression, arithmetic precision, kernel acceleration, and measured memory, energy, or wall-clock improvements.

## Development

```bash
python -m venv .venv
pip install -e .[dev]
pytest
```

Pull requests should explain what changed, why, how it was tested, and whether any claims or limitations need revision.
