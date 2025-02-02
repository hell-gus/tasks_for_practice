def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val) + f" (H={node.height})")
        if node.left or node.right:  # Если есть хотя бы один дочерний узел
            if node.left:
                print_tree(node.left, level + 1, prefix="L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, prefix="R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")