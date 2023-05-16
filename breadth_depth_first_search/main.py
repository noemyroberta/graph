from node import Node
import breadth_first_search as bfs
import depth_first_search as dfs

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# add edges
node1.neighbors = [node2, node3]
node2.neighbors = [node4]
node3.neighbors = [node4, node5]
node4.neighbors = [node5]

# starting bfs search
print("Busca em Largura:")
bfs.search(node1, 5)

# reset nodes status
node1.visited = False
node2.visited = False
node3.visited = False
node4.visited = False
node5.visited = False

# start dfs search
print("\nBusca em Profundidade:")
dfs.search(node1, 5)
