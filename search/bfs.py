from collections import deque


def bfs(graph, start, goal):
    """
    Returns
    -------
    list or None
        The path from start to goal as a list of city names,
        or None if no path exists.
    """
    if start == goal:
        return [start]

    frontier = deque([[start]])   # queue of paths
    visited = {start}

    while frontier:
        path = frontier.popleft()
        current = path[-1]

        for neighbour in graph.get(current, []):
            if neighbour in visited:
                continue
            new_path = path + [neighbour]
            if neighbour == goal:
                return new_path
            visited.add(neighbour)
            frontier.append(new_path)

    return None  # no path found
