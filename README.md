# Path Planning

> A unified research framework for classical, optimization-based, sampling-based, learning-based, and bio-inspired path planning.

**PathPlanning** is an extensible research framework for studying, implementing, visualizing, and benchmarking robotic path planning algorithms under **static, dynamic, and time-dependent environments**.

The project aims to provide a common interface for different planning paradigms, allowing algorithms such as **Dijkstra, A*, D* Lite, Theta*, RRT*, PRM, DWA, MPC, CHOMP, SAC, PPO, Genetic Algorithm, ACO, and PSO** to be evaluated under the same maps, scenarios, and metrics.

The core philosophy is:

```text
                    ┌─────────────────┐
                    │      MAP        │
                    │ Static / Dynamic│
                    │ Time-dependent  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   ENVIRONMENT   │
                    │ Collision       │
                    │ Dynamics        │
                    │ Constraints     │
                    └────────┬────────┘
                             │
                             ▼
       ┌─────────────────────┼────────────────────┐
       │                     │                    │
       ▼                     ▼                    ▼
 ┌───────────┐         ┌───────────┐        ┌───────────┐
 │  Graph    │         │ Sampling  │        │ Learning  │
 │  Search   │         │  Based    │        │  Based    │
 └─────┬─────┘         └─────┬─────┘        └─────┬─────┘
       │                     │                    │
       └─────────────────────┼────────────────────┘
                             │
                             ▼
                   ┌──────────────────┐
                   │ PATH / TRAJECTORY│
                   └─────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   EVALUATION    │
                    │ Length / Time   │
                    │ Collision       │
                    │ Smoothness      │
                    │ Clearance       │
                    └─────────────────┘
```

---

## 1. Project Goals

The project is designed around five main goals:

1. **Unified Interface**
   Provide a common API for fundamentally different path planning algorithms.

2. **Unified Map Representation**
   Support occupancy maps, cost maps, dynamic obstacles, and time-dependent environments.

3. **Algorithm Comparison**
   Compare algorithms using the same environment, start/goal states, and evaluation metrics.

4. **Reproducible Benchmarking**
   Provide configurable experiments with repeatable random seeds and standardized scenarios.

5. **Research Extensibility**
   Make it easy to add new planning algorithms, robot models, maps, and learning-based planners.

---

# 2. Repository Structure

```text
path-planning/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CITATION.cff
├── pyproject.toml
├── requirements.txt
│
├── docs/
│   ├── overview.md
│   ├── map_generation.md
│   ├── planners.md
│   ├── evaluation.md
│   └── benchmarks.md
│
├── configs/
│   ├── maps/
│   │   ├── generators/
│   │   │   ├── random_map.py
│   │   │   ├── maze.py
│   │   │   ├── warehouse.py
│   │   │   ├── indoor.py
│   │   │   ├── outdoor.py
│   │   │   ├──procedural.py
│   │   │ 
│   │   ├── dynamic_models/
│   │   │   ├── moving_point.py
│   │   │   ├── moving_circle.py
│   │   │   ├── pedestrian.py
│   │   │   └── predicted_trajectory.py
│   │   │ 
│   │   └── loaders/
│   │   │   ├── image_loader.py
│   │   │   ├── yaml_loader.py
│   │   │   └── json_loader.py
│   │   │ 
│   ├── planners/
│   └── experiments/
│
├── data/
│   ├── maps/
│   │   │
│   │   ├── static/
│   │   │   │
│   │   │   ├── empty/
│   │   │   │   ├── empty_20x20.yaml
│   │   │   │   └── empty_50x50.yaml
│   │   │   │   
│   │   │   ├── random/
│   │   │   │   ├── random_01.yaml
│   │   │   │   ├── random_02.yaml
│   │   │   │   ├── random_03.yaml
│   │   │   │   ├── random_04.yaml
│   │   │   │   └── random_05.yaml
│   │   │   │
│   │   │   ├── maze/
│   │   │   │   ├── maze_01.yaml
│   │   │   │   ├── maze_02.yaml
│   │   │   │   └── maze_03.yaml
│   │   │
│   │   │   ├── warehouse/
│   │   │   │   ├── warehouse_01.yaml
│   │   │   │   ├── warehouse_02.yaml
│   │   │   │   └── warehouse_03.yaml
│   │   │   │
│   │   │   ├── indoor/
│   │   │   │   ├── office_01.yaml
│   │   │   │   ├── office_02.yaml
│   │   │   │   └── apartment_01.yaml
│   │   │   │
│   │   │   └── outdoor/
│   │   │       ├── outdoor_01.yaml
│   │   │       ├── outdoor_02.yaml
│   │   │       └── outdoor_03.yaml

│   │
│   │   ├── dynamic/
│   │   │   ├── simple/
│   │   │   ├── warehouse/
│   │   │   ├── indoor/
│   │   │   └── pedestrian/
│   │   │
│   │   └── time_dependent/
│   │        │
│   │        ├── temporal_obstacle/
│   │        │   ├── temporal_01/
│   │        │   │   ├── metadata.yaml
│   │        │   │   ├── base_map.npy
│   │        │   │   └── temporal_rules.yaml
│   │        │   │
│   │        │   └── temporal_02/
│   │        │       ├── metadata.yaml
│   │        │       ├── base_map.npy
│   │        │       └── temporal_rules.yaml
│   │        │
│   │        ├── time_varying_cost/
│   │        │   ├── cost_01/
│   │        │   │   ├── metadata.yaml
│   │        │   │   └── cost_map.npy
│   │        │   │
│   │        │   └── cost_02/
│   │        │       ├── metadata.yaml
│   │        │       └── cost_map.npy
│   │        │
│   │        └── predicted_trajectory/
│   │            ├── prediction_01/
│   │            │   ├── metadata.yaml
│   │            │   └── trajectories.npy
│   │            │
│   │            └── prediction_02/
│   │                ├── metadata.yaml
│   │                └── trajectories.npy
│   │
│   ├── scenarios/
│   │    │
│   │    ├── static/
│   │    │   ├── easy/
│   │    │   │   ├── scenario_001.yaml
│   │    │   │   ├── scenario_002.yaml
│   │    │   │   └── scenario_003.yaml
│   │    │   │
│   │    │   ├── medium/
│   │    │   │   ├── scenario_001.yaml
│   │    │   │   └── scenario_002.yaml
│   │    │   │
│   │    │   └── hard/
│   │    │       ├── scenario_001.yaml
│   │    │       └── scenario_002.yaml
│   │    │
│   │    ├── dynamic/
│   │    │   ├── easy/
│   │    │   ├── medium/
│   │    │   └── hard/
│   │    │
│   │    └── temporal/
│   │        ├── easy/
│   │        ├── medium/
│   │        └── hard/
│   └── datasets/
│
├── src/
│   └── path_planning/
│       │
│       ├── maps/
│       │   ├── occupancy_grid.py
│       │   ├── cost_map.py
│       │   ├── dynamic_map.py
│       │   ├── temporal_map.py
│       │   ├── generators/
│       │   └── loaders/
│       │
│       ├── environment/
│       │   ├── state.py
│       │   ├── collision.py
│       │   ├── dynamics.py
│       │   └── sensors.py
│       │
│       ├── planners/
│       │   │
│       │   ├── graph_based/
│       │   ├── potential_field/
│       │   ├── sampling_based/
│       │   ├── optimization_based/
│       │   ├── trajectory_based/
│       │   ├── learning_based/
│       │   ├── bio_inspired/
│       │   └── hybrid/
│       │
│       ├── metrics/
│       │   │
│       │   ├── path_length.py
│       │   ├── planning_time.py
│       │   ├── success_rate.py
│       │   ├── collision_rate.py
│       │   ├── clearance.py
│       │   ├── smoothness.py
│       │   ├── curvature.py
│       │   ├── energy.py
│       │   └── computation_cost.py
│       │
│       ├── visualization/
│       ├── simulation/
│       └── utils/
│
├── examples/
│   ├── 01_generate_map.py
│   ├── 02_astar.py
│   ├── 03_rrt_star.py
│   ├── 04_dynamic_planning.py
│   └── 05_benchmark.py
│
├── experiments/
│   ├── static/
│   ├── dynamic/
│   └── temporal/
│
├── tests/
│
└── results/
    ├── figures/
    │
    ├── tables/
    │   └── benchmark.csv
    │
    └── logs/
        └── experiment.json
```

---

# 3. Core Architecture

The framework separates **Map**, **Environment**, **Planner**, **Path**, and **Evaluation**.

```text
Map
 │
 ├── OccupancyMap
 ├── CostMap
 ├── DynamicMap
 └── TimeDependentMap
 │
 ▼
Environment
 │
 ├── Collision Checking
 ├── Robot Dynamics
 ├── Constraints
 └── Sensors / Observations
 │
 ▼
Planner
 │
 ├── Graph-Based
 ├── Sampling-Based
 ├── Optimization-Based
 ├── Reactive / Potential Field
 ├── Trajectory / Control
 ├── Learning-Based
 └── Bio-Inspired
 │
 ▼
Path / Trajectory
 │
 ▼
Metrics
 │
 ├── Path Length
 ├── Planning Time
 ├── Collision
 ├── Clearance
 ├── Smoothness
 └── Energy
```

The separation between these components is intentional.

A planner should not need to know how a map was generated, and the evaluation module should not need to know which planner produced the path.

---

# 4. Unified Planner Interface

All planners should implement a common interface whenever possible.

A simplified planner interface is:

```python
from abc import ABC, abstractmethod


class Planner(ABC):

    @abstractmethod
    def plan(self, start, goal, environment):
        """
        Compute a path from start to goal.
        """
        pass
```

A planner can then be used as:

```python
planner = AStar()

result = planner.plan(
    start=start,
    goal=goal,
    environment=environment
)
```

The planner returns a unified planning result:

```python
result.path
result.cost
result.success
result.planning_time
result.iterations
```

For example:

```python
planners = [
    Dijkstra(),
    AStar(),
    ThetaStar(),
    RRTStar(),
]

for planner in planners:

    result = planner.plan(
        start=start,
        goal=goal,
        environment=environment
    )

    evaluator.evaluate(result)
```

This allows completely different algorithms to be evaluated using the same experiment pipeline.

---

# 5. Map Representation

The framework supports multiple levels of environmental representation.

## 5.1 Occupancy Map

A binary representation:

```text
0 → Free
1 → Occupied
```

Conceptually:

```text
M(x, y) ∈ {0, 1}
```

Useful for:

* Grid search
* A*
* Dijkstra
* Theta*
* JPS

---

## 5.2 Static Cost Map

A continuous cost representation:

```text
C(x, y) ≥ 0
```

Example:

```text
Low cost       → preferred region
High cost      → undesirable region
Infinite cost  → obstacle
```

This allows planners to optimize not only distance but also:

* obstacle clearance
* terrain cost
* risk
* energy
* traversability

---

## 5.3 Dynamic Cost Map

The environment changes over time:

```text
C(x, y, t)
```

Examples:

* moving pedestrians
* moving vehicles
* dynamic obstacles
* changing terrain
* changing risk regions

Relevant planners include:

* D*
* D* Lite
* RRTx
* DWA
* MPC
* Reinforcement Learning

---

## 5.4 Time-Dependent Map

A more general representation:

```text
C(x, y, t)
```

or, for state-dependent planning:

```text
C(x, y, θ, v, t)
```

This allows the framework to study:

* time-dependent obstacles
* predicted obstacle trajectories
* velocity constraints
* temporal planning
* kinodynamic planning

---

# 6. Map Generation

Maps should be generated independently from planners.

```text
maps/
│
├── generators/
│   ├── random_map.py
│   ├── maze.py
│   ├── warehouse.py
│   ├── indoor.py
│   ├── outdoor.py
│   └── procedural.py
│
├── dynamic_models/
│   ├── moving_point.py
│   ├── moving_circle.py
│   ├── pedestrian.py
│   └── predicted_trajectory.py
│
└── loaders/
    ├── image_loader.py
    ├── yaml_loader.py
    └── json_loader.py
```

Example:

```python
environment = RandomMap(
    width=100,
    height=100,
    obstacle_density=0.2,
    seed=42
)
```

The same environment can then be passed to:

```text
A*
D*
Theta*
RRT*
DWA
SAC
ACO
```

without modifying the map.

---

# 7. Algorithms

## Overview

| Category             | Algorithms        | Static | Dynamic |    Optimal   | Real-time |
| -------------------- | ----------------- | :----: | :-----: | :----------: | :-------: |
| Graph / Search       | BFS               |    ✓   |         |      ✓*      |     ✓     |
| Graph / Search       | Dijkstra          |    ✓   |    △    |       ✓      |     ✓     |
| Graph / Search       | A*                |    ✓   |    △    |      ✓*      |     ✓     |
| Graph / Search       | D*                |        |    ✓    |      ✓*      |     ✓     |
| Graph / Search       | D* Lite           |        |    ✓    |      ✓*      |     ✓     |
| Graph / Search       | Theta*            |    ✓   |    △    |      ✓*      |     ✓     |
| Graph / Search       | JPS               |    ✓   |         |      ✓*      |     ✓     |
| Reactive             | APF               |    ✓   |    ✓    |              |     ✓     |
| Reactive             | VFH               |    ✓   |    ✓    |              |     ✓     |
| Sampling             | PRM               |    ✓   |         |              |     △     |
| Sampling             | RRT               |    ✓   |    △    |              |     △     |
| Sampling             | RRT-Connect       |    ✓   |    △    |              |     ✓     |
| Sampling             | RRT*              |    ✓   |    △    | Asymptotic ✓ |     △     |
| Sampling             | Informed RRT*     |    ✓   |    △    | Asymptotic ✓ |     △     |
| Sampling             | RRTx              |        |    ✓    |       △      |     ✓     |
| Optimization         | CHOMP             |    ✓   |    △    |       △      |     △     |
| Optimization         | STOMP             |    ✓   |    △    |       △      |     △     |
| Optimization         | TrajOpt           |    ✓   |    △    |       △      |     △     |
| Trajectory / Control | DWA               |    ✓   |    ✓    |              |     ✓     |
| Trajectory / Control | TEB               |    ✓   |    ✓    |              |     ✓     |
| Trajectory / Control | MPC               |    ✓   |    ✓    |       △      |     ✓     |
| Learning             | DQN               |    ✓   |    ✓    |              |     ✓     |
| Learning             | PPO               |    ✓   |    ✓    |              |     ✓     |
| Learning             | SAC               |    ✓   |    ✓    |              |     ✓     |
| Learning             | GNN Planner       |    ✓   |    ✓    |              |     △     |
| Learning             | Diffusion Planner |    ✓   |    ✓    |              |     △     |
| Bio-inspired         | GA                |    ✓   |    △    |              |     △     |
| Bio-inspired         | ACO               |    ✓   |    △    |              |     △     |
| Bio-inspired         | PSO               |    ✓   |    △    |              |     △     |
| Bio-inspired         | DE                |    ✓   |    △    |              |     △     |
| Bio-inspired         | GWO               |    ✓   |    △    |              |     △     |
| Bio-inspired         | WOA               |    ✓   |    △    |              |     △     |

### Legend

```text
✓  Supported / generally suitable
△  Possible, but highly dependent on implementation and problem formulation
*  Optimal under specific assumptions
```

The table describes the typical properties of the algorithm family rather than an absolute guarantee for every implementation.

---

# 8. Graph / Search-Based Planning

Graph-based planners discretize the environment into nodes and edges and search for a path.

### Algorithms

```text
BFS
Dijkstra
A*
D*
D* Lite
LPA*
Theta*
Lazy Theta*
JPS
ANYA
Bidirectional A*
```

### Strengths

* Deterministic behavior
* Strong theoretical foundations
* Easy to benchmark
* Excellent for grid-based maps
* A* can provide optimal paths under appropriate cost/admissibility assumptions
* D* / D* Lite are suitable for changing environments

### Weaknesses

* Grid resolution affects performance
* High-dimensional state spaces become expensive
* Classical graph search does not naturally handle complex vehicle dynamics
* Replanning may become expensive for large maps

### Typical applications

```text
2D mobile robot
warehouse robot
AGV
grid navigation
indoor navigation
global planning
```

---

# 9. Potential Field / Reactive Planning

Potential-field methods construct attractive and repulsive fields.

The basic idea is:

```text
Goal
 ↓
Attractive Force

Obstacle
 ↓
Repulsive Force
```

Typical methods:

```text
APF
VFF
VFH
Elastic Band
```

### Advantages

* Very simple
* Computationally efficient
* Suitable for local navigation
* Easy to integrate with sensor-based navigation
* Good real-time characteristics

### Disadvantages

* Local minima
* Oscillation
* Goal non-reachability in some configurations
* Sensitive to parameter tuning
* Difficult to guarantee global optimality

APF is therefore generally better considered a **reactive / potential-field method** rather than a data-based planning method.

---

# 10. Sampling-Based Planning

Sampling-based planners avoid explicitly constructing the entire configuration-space graph.

Typical algorithms:

```text
PRM
PRM*
RRT
RRT-Connect
RRT*
Informed RRT*
RRT#
RRTx
FMT*
BIT*
```

### Advantages

* Suitable for high-dimensional spaces
* Works well with continuous configuration spaces
* Naturally handles complicated geometry
* RRT/RRT-Connect can find feasible paths quickly
* RRT* provides asymptotic optimality under appropriate assumptions

### Disadvantages

* Randomness
* Path quality can initially be poor
* Convergence can be slow
* Results can vary between runs
* Collision checking can become computationally expensive

Sampling-based planning is particularly useful for:

```text
Manipulator planning
SE(2)
SE(3)
High-dimensional configuration spaces
Kinodynamic planning
```

---

# 11. Optimization-Based Planning

Optimization-based methods formulate planning as an optimization problem.

A generic objective can be written as:

```text
J =
    w_length    J_length
  + w_collision J_collision
  + w_smooth    J_smooth
  + w_clearance J_clearance
  + w_energy    J_energy
```

Typical algorithms:

```text
CHOMP
STOMP
TrajOpt
GPMP
Gradient-based trajectory optimization
Sequential convex optimization
```

### Advantages

* Produces smooth trajectories
* Can directly optimize multiple objectives
* Can incorporate constraints
* Particularly useful for robot manipulators and trajectory generation

### Disadvantages

* Local minima
* Sensitive to initialization
* Computational cost can be significant
* Usually does not provide global optimality
* Requires careful objective and constraint design

---

# 12. Trajectory / Control-Based Planning

These methods consider not only where the robot should go, but also how it should move.

Typical methods:

```text
DWA
TEB
MPC
LQR
Kinodynamic A*
Kinodynamic RRT
```

### DWA

DWA searches in velocity space and evaluates feasible short-term trajectories.

Advantages:

* Fast
* Reactive
* Naturally considers velocity constraints
* Very suitable for mobile robots

Disadvantages:

* Local planner
* Short horizon
* Can get trapped by poor local decisions
* Global optimality is not guaranteed

---

## MPC

Model Predictive Control repeatedly solves an optimization problem over a future horizon.

Advantages:

* Handles dynamics and constraints
* Can optimize trajectory and control together
* Very useful for autonomous vehicles and mobile robots

Disadvantages:

* Computationally expensive
* Requires a reasonable robot model
* Sensitive to prediction horizon and cost function

---

# 13. Learning-Based Planning

Learning-based planning learns a policy, value function, trajectory distribution, or planning representation from data.

```text
learning_based/
│
├── supervised/
├── imitation_learning/
├── reinforcement_learning/
├── graph_learning/
├── transformer/
├── diffusion/
└── meta_learning/
```

### Supervised Learning

Examples:

```text
CNN Planner
MLP Planner
Transformer Planner
GNN Planner
```

Advantages:

* Fast inference after training
* Can learn complex representations
* Can exploit large datasets

Disadvantages:

* Requires training data
* Generalization can be difficult
* Safety guarantees are difficult
* Distribution shift can significantly degrade performance

---

## Imitation Learning

Examples:

```text
Behavior Cloning
DAgger
Inverse Reinforcement Learning
```

The planner learns from expert demonstrations.

Advantages:

* Can learn complex expert behaviors
* Easier than manually designing a complete cost function

Disadvantages:

* Requires expert demonstrations
* Compounding errors
* Distribution shift
* Quality depends strongly on demonstrations

---

## Reinforcement Learning

Examples:

```text
DQN
DDPG
TD3
PPO
SAC
```

Advantages:

* Does not necessarily require labeled trajectories
* Can optimize long-term objectives
* Suitable for dynamic environments
* Can learn complex reactive behavior

Disadvantages:

* Training can be expensive
* Reward engineering is difficult
* Safety is challenging
* Sim-to-real transfer can be problematic

---

# 14. Bio-Inspired / Metaheuristic Planning

Bio-inspired methods treat planning as a population-based or heuristic optimization problem.

```text
Genetic Algorithm
Differential Evolution
Ant Colony Optimization
Particle Swarm Optimization
Artificial Bee Colony
Firefly Algorithm
Bat Algorithm
Grey Wolf Optimizer
Whale Optimization Algorithm
Harmony Search
```

### Advantages

* Flexible objective functions
* Can optimize non-convex problems
* Easy to combine multiple objectives
* Does not require gradients

### Disadvantages

* Often computationally expensive
* Parameter-sensitive
* No general guarantee of global optimality
* Convergence can be slow
* Reproducibility can be affected by stochasticity

These methods are particularly useful as **research / optimization baselines**, but should generally be distinguished from classical graph-search and sampling-based methods.

---

# 15. Hybrid Planning

Real robotic systems often combine multiple planners.

A common architecture is:

```text
Global Planner
      │
      ▼
Local Planner
      │
      ▼
Trajectory Optimizer
      │
      ▼
Controller
```

Examples:

```text
A* + DWA
A* + MPC
RRT* + CHOMP
RRT* + MPC
Learning + A*
Learning + MPC
RL + Classical Planner
```

Hybrid planning is useful because different algorithms solve different parts of the navigation problem.

For example:

```text
A*
→ global route

DWA
→ local obstacle avoidance

MPC
→ trajectory tracking
```

---

# 16. Evaluation Metrics

All planners should be evaluated using common metrics.

```text
metrics/
│
├── path_length.py
├── planning_time.py
├── success_rate.py
├── collision_rate.py
├── clearance.py
├── smoothness.py
├── curvature.py
├── energy.py
└── computation_cost.py
```

Core metrics include:

| Metric            | Description                                |
| ----------------- | ------------------------------------------ |
| Path Length       | Total geometric path length                |
| Planning Time     | Time required to generate a solution       |
| Success Rate      | Percentage of successful planning attempts |
| Collision Rate    | Frequency of collision                     |
| Minimum Clearance | Minimum distance to obstacles              |
| Average Clearance | Average distance from obstacles            |
| Smoothness        | Measure of trajectory smoothness           |
| Curvature         | Path curvature characteristics             |
| Energy            | Estimated motion/control energy            |
| Iterations        | Number of search/optimization iterations   |
| Nodes             | Number of explored/generated nodes         |
| Memory            | Memory consumption                         |

---

# 17. Benchmarking

The same environment should be used for different algorithms.

For example:

```text
Environment
    │
    ├── A*
    ├── D* Lite
    ├── Theta*
    ├── RRT*
    ├── DWA
    ├── MPC
    ├── SAC
    └── ACO
          │
          ▼
       Metrics
          │
          ▼
    Comparison
```

Example:

```bash
python examples/05_benchmark.py \
    --map warehouse_01 \
    --planners astar dstar_lite theta_star rrt_star \
    --runs 100 \
    --seed 42
```

The benchmark can produce:

```text
results/
│
├── figures/
│   ├── paths.png
│   ├── planning_time.png
│   ├── path_length.png
│   └── clearance.png
│
├── tables/
│   └── benchmark.csv
│
└── logs/
    └── experiment.json
```

---

# 18. Example Workflow

## Generate a Map

```python
from path_planning.maps import RandomMap

environment = RandomMap(
    width=100,
    height=100,
    obstacle_density=0.2,
    seed=42
)
```

## Select a Planner

```python
from path_planning.planners.graph_based import AStar

planner = AStar()
```

## Plan

```python
result = planner.plan(
    start=(5, 5),
    goal=(90, 90),
    environment=environment
)
```

## Evaluate

```python
from path_planning.metrics import Evaluator

evaluator = Evaluator()

metrics = evaluator.evaluate(result)

print(metrics)
```

## Visualize

```python
from path_planning.visualization import plot_path

plot_path(
    environment,
    result.path
)
```

---

# 19. Static vs Dynamic Planning

The framework distinguishes three major planning scenarios.

### Static

```text
Map
 ↓
Planner
 ↓
Path
```

Typical algorithms:

```text
Dijkstra
A*
Theta*
PRM
RRT*
CHOMP
GA
ACO
```

---

### Dynamic

```text
Environment(t)
      ↓
Planner
      ↓
Replanning
      ↓
Updated Path
```

Typical algorithms:

```text
D*
D* Lite
RRTx
DWA
TEB
MPC
RL
```

---

### Time-Dependent

```text
C(x, y, t)
      ↓
Spatiotemporal Planning
      ↓
Trajectory
```

The planner must consider both:

```text
where
+
when
```

This is especially important for:

```text
autonomous vehicles
mobile robots
multi-agent navigation
pedestrian environments
dynamic obstacle avoidance
```

---

# 20. Research Benchmark Matrix

A long-term goal of this project is to create a benchmark matrix:

```text
                         Static   Dynamic   Temporal
------------------------------------------------------
Dijkstra                    ✓
A*                          ✓
D* Lite                              ✓
Theta*                      ✓
RRT*                        ✓
RRTx                                  ✓
DWA                                    ✓
MPC                                    ✓
SAC                         ✓          ✓         ✓
ACO                         ✓          △
PSO                         ✓          △
```

Each algorithm can be evaluated across:

```text
Map Type
    ×
Obstacle Density
    ×
Environment Dynamics
    ×
Robot Model
    ×
Planning Algorithm
```

This makes the repository useful not only as an implementation collection but also as a **research benchmark platform**.

---

# 21. Design Principles

The project follows several design principles.

### 1. Separation of Concerns

```text
Map ≠ Planner ≠ Evaluation
```

A planner should not generate its own map.

---

### 2. Reproducibility

Experiments should support:

```text
Random Seed
Configuration Files
Fixed Scenarios
Multiple Runs
Saved Results
```

---

### 3. Common Interface

Different algorithms should expose a similar API:

```python
result = planner.plan(
    start,
    goal,
    environment
)
```

---

### 4. Algorithm Independence

Adding a new planner should not require modification of:

```text
Map
Environment
Metrics
Visualization
Benchmark
```

---

### 5. Research First

The framework prioritizes:

```text
Reproducibility
Comparability
Extensibility
Visualization
Benchmarking
```

rather than simply maximizing the number of implemented algorithms.

---

# 22. Roadmap

## Phase 1 — Core Framework

* [ ] Occupancy Grid
* [ ] Static Cost Map
* [ ] Map Generator
* [ ] Unified Planner Interface
* [ ] Path Data Structure
* [ ] Collision Checker
* [ ] Visualization
* [ ] Basic Metrics

## Phase 2 — Classical Planning

* [ ] BFS
* [ ] Dijkstra
* [ ] A*
* [ ] Theta*
* [ ] Lazy Theta*
* [ ] JPS
* [ ] D*
* [ ] D* Lite
* [ ] LPA*

## Phase 3 — Sampling-Based Planning

* [ ] PRM
* [ ] PRM*
* [ ] RRT
* [ ] RRT-Connect
* [ ] RRT*
* [ ] Informed RRT*
* [ ] RRTx
* [ ] BIT*

## Phase 4 — Local and Optimization Planning

* [ ] APF
* [ ] VFH
* [ ] DWA
* [ ] TEB
* [ ] CHOMP
* [ ] STOMP
* [ ] TrajOpt
* [ ] MPC

## Phase 5 — Dynamic Environment

* [ ] Dynamic Obstacles
* [ ] Moving Obstacles
* [ ] Predicted Obstacle Trajectories
* [ ] Time-dependent Cost Maps
* [ ] Replanning Benchmark

## Phase 6 — Learning-Based Planning

* [ ] Behavior Cloning
* [ ] DAgger
* [ ] DQN
* [ ] PPO
* [ ] SAC
* [ ] GNN Planner
* [ ] Transformer Planner
* [ ] Diffusion Planner

## Phase 7 — Bio-Inspired Planning

* [ ] Genetic Algorithm
* [ ] Differential Evolution
* [ ] ACO
* [ ] PSO
* [ ] Artificial Bee Colony
* [ ] Firefly Algorithm
* [ ] Grey Wolf Optimizer
* [ ] Whale Optimization Algorithm

## Phase 8 — Hybrid Planning

* [ ] A* + DWA
* [ ] A* + MPC
* [ ] RRT* + CHOMP
* [ ] RRT* + MPC
* [ ] Learning + Classical Planning
* [ ] Learning + MPC

---

# 23. Contributing

Contributions are welcome.

When adding a new planner, please provide:

```text
1. Algorithm implementation
2. Planner interface
3. Configuration
4. Example
5. Unit tests
6. Documentation
7. Benchmark results
```

A new algorithm should preferably implement:

```python
class MyPlanner(Planner):

    def plan(
        self,
        start,
        goal,
        environment
    ):
        ...
```

and return the standard planning result.

---

# 24. Citation

If you use this repository in academic research, please cite:

```text
Coming soon
```

A `CITATION.cff` file will be provided once the project reaches its first stable release.

---

# 25. License

This project is released under the MIT License.

See [LICENSE](LICENSE) for details.

---

# 26. Project Vision

The long-term goal is to build a unified platform where researchers can answer questions such as:

> Which planner performs best for a given environment?

> How does map complexity affect planning performance?

> How does dynamic obstacle density affect different planning paradigms?

> What is the trade-off between planning time, path quality, safety, and optimality?

> Can learning-based planners outperform classical planners under dynamic environments?

> Which hybrid planning architecture provides the best performance for a particular robot?

Ultimately:

```text
                 PATH PLANNING
                       │
        ┌──────────────┼──────────────┐
        │              │              │
      MAP          PLANNERS       ROBOTS
        │              │              │
        └──────────────┼──────────────┘
                       │
                   SCENARIOS
                       │
                       ▼
                   BENCHMARK
                       │
                       ▼
                   COMPARISON
                       │
                       ▼
                   RESEARCH
```

**PathPlanning is intended to become a reproducible and extensible platform for robotic path planning research.**
