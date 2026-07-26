# Methodology

The hypothesis is that numerical precision can be allocated dynamically according to learning activity.

The initial controller maps a scalar activity signal to an allowed bit width using deterministic thresholds. The lightweight repository demonstration uses mean absolute gradient magnitude. Fake quantization simulates signed symmetric uniform quantization while retaining floating-point tensors.

Effective precision is the mean assigned bit width across allocation events. It is a comparison proxy, not a direct measurement of memory, latency, throughput, or energy.
