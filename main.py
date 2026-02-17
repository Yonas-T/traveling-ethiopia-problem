
from graphs.figure1_graph import figure1_graph
from graphs.figure2_graph import figure2_graph
from graphs.figure3_graph import figure3_graph, figure3_heuristics
from graphs.figure4_game_tree import game_tree, terminal_utilities

from search.bfs import bfs
from search.dfs import dfs
from search.ucs import ucs, multi_goal_ucs
from search.astar import astar
from search.minimax import minimax_decision


# ─────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────

def print_header(title):
    line = "═" * 60
    print(f"\n{line}")
    print(f"  {title}")
    print(f"{line}")


def print_path(label, path, cost=None):
    if path is None:
        print(f"  {label}: No path found!")
    else:
        print(f"  {label}:")
        print(f"    Path : {' → '.join(path)}")
        print(f"    Steps: {len(path) - 1}")
        if cost is not None:
            print(f"    Cost : {cost}")


# ─────────────────────────────────────────────
#  Q1 — Breadth-First Search & Depth-First Search
# ─────────────────────────────────────────────

def run_q1():
    print_header("Q1 — BFS & DFS  (Figure 1: Unweighted Graph)")

    pairs = [
        ("Addis Ababa", "Lalibela"),
        ("Addis Ababa", "Moyale"),
        ("Asmera", "Arba Minch"),
    ]

    for start, goal in pairs:
        print(f"\n  ▸ {start}  ⟶  {goal}")

        path_bfs = bfs(figure1_graph, start, goal)
        print_path("BFS", path_bfs)

        path_dfs = dfs(figure1_graph, start, goal)
        print_path("DFS", path_dfs)


# ─────────────────────────────────────────────
#  Q2 — Uniform Cost Search
# ─────────────────────────────────────────────

def run_q2():
    print_header("Q2.2 — UCS: Addis Ababa → Lalibela  (Figure 2)")

    path, cost = ucs(figure2_graph, "Addis Ababa", "Lalibela")
    print_path("UCS", path, cost)

    print_header("Q2.3 — Multi-Goal UCS: Tourist Route  (Figure 2)")
    goals = [
        "Axum", "Gondar", "Lalibela", "Babile",
        "Jimma", "Bale", "Sof Oumer", "Arba Minch",
    ]
    print(f"  Start : Addis Ababa")
    print(f"  Goals : {', '.join(goals)}")

    full_path, total_cost = multi_goal_ucs(figure2_graph, "Addis Ababa", goals)
    print(f"\n  Full tour path:")
    print(f"    {' → '.join(full_path)}")
    print(f"  Total cost: {total_cost}")

    # Show order of goals visited
    visited_order = [city for city in full_path if city in goals]
    # Remove duplicates while preserving order
    seen = set()
    order = []
    for c in visited_order:
        if c not in seen:
            seen.add(c)
            order.append(c)
    print(f"  Goals visited in order: {' → '.join(order)}")


# ─────────────────────────────────────────────
#  Q3 — A* Search
# ─────────────────────────────────────────────

def run_q3():
    print_header("Q3 — A* Search: Addis Ababa → Moyale  (Figure 3)")

    path, cost = astar(
        figure3_graph, "Addis Ababa", "Moyale", figure3_heuristics
    )
    print_path("A*", path, cost)


# ─────────────────────────────────────────────
#  Q4 — MiniMax Search
# ─────────────────────────────────────────────

def run_q4():
    print_header("Q4 — MiniMax: Adversarial Search  (Figure 4)")

    value, path = minimax_decision(
        "Addis Ababa", game_tree, terminal_utilities
    )

    print(f"  Root        : Addis Ababa  (MAX)")
    print(f"  Best value  : {value}")
    print(f"  Optimal path: {' → '.join(path)}")
    print(f"  Best move   : {path[1] if len(path) > 1 else 'N/A'}")

    # Show the full tree evaluation
    print(f"\n  Detailed MiniMax evaluation:")
    for child in game_tree["Addis Ababa"]:
        # MIN level
        child_vals = []
        for grandchild in game_tree[child]:
            # MAX level — these lead to terminals
            gc_vals = []
            for terminal in game_tree[grandchild]:
                gc_vals.append(f"{terminal}={terminal_utilities[terminal]}")
            max_val = max(terminal_utilities[t] for t in game_tree[grandchild])
            child_vals.append(f"    {grandchild} (MAX): {', '.join(gc_vals)} → max={max_val}")
        min_val = min(
            max(terminal_utilities[t] for t in game_tree[gc])
            for gc in game_tree[child]
        )
        print(f"  {child} (MIN) → min={min_val}")
        for cv in child_vals:
            print(cv)

    overall = max(
        min(
            max(terminal_utilities[t] for t in game_tree[gc])
            for gc in game_tree[child]
        )
        for child in game_tree["Addis Ababa"]
    )
    print(f"\n  Addis Ababa (MAX) → max = {overall}")


# ─────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "▓" * 60)
    print("  TRAVELING ETHIOPIA PROBLEM — Course Project")
    print("  AI: Principles and Techniques — AAiT")
    print("▓" * 60)

    run_q1()
    run_q2()
    run_q3()
    run_q4()

    print("\n" + "═" * 60)
    print("  Done!  All questions executed successfully.")
    print("═" * 60 + "\n")
