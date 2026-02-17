# Traveling Ethiopia Problem

## Overview

This project is Traveling Ethiopia Problem, implementing various AI search algorithms on a state-space graph of Ethiopian cities.

## Project Structure

```
traveling-ethiopia-problem/
├── main.py                    # Run all questions
├── graphs/
│   ├── figure1_graph.py       # Unweighted adjacency list
│   ├── figure2_graph.py       # Weighted adjacency list (backward costs)
│   ├── figure3_graph.py       # Weighted graph + heuristic values
│   └── figure4_game_tree.py   # Adversarial game tree
├── search/
│   ├── bfs.py                 # Breadth-First Search
│   ├── dfs.py                 # Depth-First Search
│   ├── ucs.py                 # Uniform Cost Search + Multi-Goal UCS
│   ├── astar.py               # A* Search
│   └── minimax.py             # MiniMax Search
└── README.md
```

## How to Run

```bash
# Python 3.7+ 
python main.py
```

## Algorithms

### Breadth-First Search (BFS)
Explores nodes level by level using a FIFO queue. Guarantees the shortest path in terms of number of hops on unweighted graphs.

### Depth-First Search (DFS)
Explores as deep as possible before backtracking, using a LIFO stack.

### Uniform Cost Search (UCS)
Expands the node with the lowest cumulative path cost using a priority queue. The multi-goal variant uses a greedy nearest-unvisited approach to visit all tourist destinations.

### A* Search
Combines backward cost g(n) with a heuristic estimate h(n) using f(n) = g(n) + h(n). The goal is to generate a path from the initial state “Addis Ababa” to goal state “Moyale”. 

### MiniMax Search
Used for adversarial search. The agent (MAX) tries to maximize utility while the adversary (MIN) tries to minimize it. The goal of the agent is to reach to a state where it gains good quality of Coffee.

## Tourist Cities (Q2.3)

The multi-goal UCS visits these destinations starting from Addis Ababa:
- **Axum** — Ancient obelisks
- **Gondar** — Royal castles
- **Lalibela** — Rock-hewn churches
- **Babile** — Elephant sanctuary
- **Jimma** — Coffee heritage
- **Bale** — Mountain nyala
- **Sof Oumer** — Sof Omar caves
- **Arba Minch** — Nechisar National Park
