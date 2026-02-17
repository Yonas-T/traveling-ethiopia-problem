def dfs(graph, start, goal):
    """
    Returns
    -------
    list or None
        A path from start to goal as a list of city names,
        or None if no path exists.
    """
    if start == goal:
        return [start]

    frontier = [[start]]   # stack of paths
    visited = set()

    while frontier:
        path = frontier.pop()
        current = path[-1]

        if current in visited:
            continue
        visited.add(current)

        for neighbour in graph.get(current, []):
            if neighbour in visited:
                continue
            new_path = path + [neighbour]
            if neighbour == goal:
                return new_path
            frontier.append(new_path)

    return None  # no path found
