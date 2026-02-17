def minimax(node, is_maximizing, game_tree, utilities):
    """
    Returns
    -------
    (int, str)
        (best_value, best_child) — the optimal utility and the
        immediate child chosen at this node.  For leaf nodes
        best_child is None.
    """
    if node in utilities:
        return utilities[node], None

    children = game_tree.get(node, [])
    if not children:
        return 0, None

    if is_maximizing:
        best_value = float("-inf")
        best_child = None
        for child in children:
            value, _ = minimax(child, False, game_tree, utilities)
            if value > best_value:
                best_value = value
                best_child = child
        return best_value, best_child
    else:
        best_value = float("inf")
        best_child = None
        for child in children:
            value, _ = minimax(child, True, game_tree, utilities)
            if value < best_value:
                best_value = value
                best_child = child
        return best_value, best_child


def minimax_decision(root, game_tree, utilities):
    """
    Returns
    -------
    (int, list[str])
        (best_value, path_from_root_to_leaf)
    """
    value, best_child = minimax(root, True, game_tree, utilities)

    path = [root]
    current = root
    is_max = True
    while current in game_tree:
        _, chosen = minimax(current, is_max, game_tree, utilities)
        if chosen is None:
            break
        path.append(chosen)
        current = chosen
        is_max = not is_max

    return value, path
