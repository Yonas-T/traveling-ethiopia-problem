import heapq


def ucs(graph, start, goal):
    """
    Returns
    -------
    (list, float) or (None, float('inf'))
        A tuple of (path, total_cost).
    """
    if start == goal:
        return [start], 0

    counter = 0
    frontier = [(0, counter, [start])]
    visited = set()

    while frontier:
        cost, _, path = heapq.heappop(frontier)
        current = path[-1]

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, cost

        for neighbour, edge_cost in graph.get(current, []):
            if neighbour not in visited:
                counter += 1
                heapq.heappush(frontier, (cost + edge_cost, counter, path + [neighbour]))

    return None, float("inf")


def multi_goal_ucs(graph, start, goals):
    """
    Returns
    -------
    (list, float)
        The full path visiting all goals and its total cost.
    """
    remaining = set(goals)
    current = start
    full_path = [start]
    total_cost = 0

    while remaining:
        best_path = None
        best_cost = float("inf")
        best_goal = None

        for goal in remaining:
            path, cost = ucs(graph, current, goal)
            if path is not None and cost < best_cost:
                best_cost = cost
                best_path = path
                best_goal = goal

        if best_path is None:
            print(f"  ⚠  No path from {current} to any remaining goal!")
            break

        full_path.extend(best_path[1:])
        total_cost += best_cost
        remaining.remove(best_goal)
        current = best_goal

    return full_path, total_cost
