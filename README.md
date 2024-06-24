# Travelling Salesman Problem Solver

This project implements two algorithms for solving the Travelling Salesman Problem (TSP).

## Algorithms Implemented

1. **Tabu Search**
2. **Simulated Annealing**

## Problem Description

The Travelling Salesman Problem requires finding the shortest possible route that allows a salesman to visit each city exactly once and return to the starting city. The distance between cities is calculated using the Euclidean distance formula.

## Features

- **Console Interface**: Allows user to set number of cities and choose the algorithm.
- **Seed Option**: Ensures reproducibility by generating the same set of random cities using a seed.
- **Algorithm Selection**: Choose between Tabu Search and Simulated Annealing to solve the TSP.
- **Run-Time Information**: Displays current state during algorithm execution, such as iteration count and path length (or temperature for Simulated Annealing).
- **Final Output**: Shows the optimal path length and visual representation of the route and cities.

## Implementation Details

### Tabu Search

- **Representation**: Uses a vector with city indices representing a permutation of cities.
- **Tabu List**: Manages forbidden moves to prevent cycling through local optima.
- **Parameters**: Includes tabu list length to balance exploration and exploitation.

### Simulated Annealing

- **Representation**: Also uses a vector with city indices representing a permutation of cities.
- **Temperature Schedule**: Defines how the probability of accepting worse solutions decreases over time.
- **Parameters**: Includes initial temperature and cooling schedule to control exploration.

## Documentation

The detailed documentation of this project includes:

- **Algorithm Descriptions**: Detailed explanations of Tabu Search and Simulated Annealing, including their respective data representations and key parameters.
- **Implementation Strategies**: Insights into how each algorithm was implemented, highlighting crucial decision points such as neighborhood exploration and solution evaluation.
- **Performance Evaluation**: Analysis of algorithm performance on different problem sizes.
- **Comparison**: A comparative study of Tabu Search and Simulated Annealing, discussing their strengths and weaknesses in solving the TSP.
- **Visualization**: Description of how results are visualized, providing clarity on the optimal path and city layout.

For detailed documentation, please check [Technical Documentation](Dokumentacia_UI_P2.pdf) in the repository.
