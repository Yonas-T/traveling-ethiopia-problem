import heapq


def astar(graph, start, goal, heuristics):
    """
    Returns
    -------
    (list, float) or (None, float('inf'))
        A tuple of (path, total_cost).
    """
    if start == goal:
        return [start], 0

    counter = 0
    f0 = heuristics.get(start, 0)
    frontier = [(f0, counter, 0, [start])]
    best_g = {start: 0}

    while frontier:
        f_cost, _, g_cost, path = heapq.heappop(frontier)
        current = path[-1]

        if current == goal:
            return path, g_cost

        if g_cost > best_g.get(current, float("inf")):
            continue

        for neighbour, edge_cost in graph.get(current, []):
            new_g = g_cost + edge_cost
            if new_g < best_g.get(neighbour, float("inf")):
                best_g[neighbour] = new_g
                h = heuristics.get(neighbour, 0)
                f = new_g + h
                counter += 1
                heapq.heappush(frontier, (f, counter, new_g, path + [neighbour]))

    return None, float("inf")
