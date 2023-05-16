def search(start_node, target_value):
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)
        print("Visitando o nó:", current_node.value)

        if current_node.value == target_value:
            print("Valor encontrado!")
            return True

        current_node.visited = True

        for neighbor in current_node.neighbors:
            if not neighbor.visited:
                queue.append(neighbor)

    print("Valor não encontrado.")
    return False

