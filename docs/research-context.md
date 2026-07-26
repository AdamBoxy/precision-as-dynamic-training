# Research Context

Neighboring areas include automatic mixed precision, loss scaling, quantization-aware training, FP8 training, low-bit optimizers, layerwise precision assignment, and hardware-aware optimization.

This repository separates three questions:

1. Can a learning signal choose precision without destabilizing training?
2. Can the policy reduce a meaningful precision-cost proxy while preserving quality?
3. Can kernels and hardware convert that policy into measured savings?

The current work addresses the first and begins the second. It does not answer the third.
