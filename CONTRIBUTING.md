# Contributing to Path Planning Research Framework

Thank you for your interest in contributing to this project.

This repository is designed as a unified and extensible research framework
for robotic path planning, including classical, sampling-based,
optimization-based, trajectory-based, learning-based, bio-inspired,
and hybrid planning methods.

Contributions are welcome in the following areas:

- New path planning algorithms
- Improvements to existing planners
- New map generators
- New environment models
- New robot models
- New evaluation metrics
- Benchmark scenarios
- Learning-based datasets and models
- Visualization tools
- Simulation tools
- Documentation
- Bug fixes
- Performance improvements
- Reproducibility improvements

---

## 1. Project Structure

The repository separates algorithms, configurations, data, experiments,
and evaluation.

```text
src/
    path_planning/
        maps/
        environment/
        planners/
        metrics/
        visualization/
        simulation/
        utils/

configs/
    maps/
    planners/
    experiments/

data/
    maps/
    scenarios/
    datasets/

experiments/
    static/
    dynamic/
    temporal/

tests/
