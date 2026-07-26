# Limitations

- Fake quantization is not native low-bit execution.
- The experimental setting is intentionally small.
- Threshold policies may be sensitive to signal scale, optimizer, batch size, normalization, learning rate, and seed.
- Mean effective bits are not equivalent to measured systems savings.
- Dynamic and adaptive precision have a substantial prior literature; this work is framed as a reproducible systems hypothesis and controller experiment.
- The included synthetic script is not the exact archived Kaggle experiment.
