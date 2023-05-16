def search(current_node, target_value):
    print("Visitando o nó:", current_node.value)

    if current_node.value == target_value:
        print("Valor encontrado!")
        return True

    current_node.visited = True

    for neighbor in current_node.neighbors:
        if not neighbor.visited:
            if search(neighbor, target_value):
                return True

    return False
