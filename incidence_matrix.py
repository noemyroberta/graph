class IncidenceMatrix:
    vertices_size = 0
    edges_size = 0
    matrix = 0

    # vertices are lines
    # edges are columns
    def __init__(self, vertices_size, edges_size):
        self.vertices_size = vertices_size
        self.edges_size = edges_size
        self.matrix = [[0 for _ in range(edges_size)] for _ in range(vertices_size)]

    def __str__(self):
        graph = ''

        for i in range(self.vertices_size):
            for j in range(self.edges_size):
                graph += str(self.matrix[i][j]) + ' '
            graph += '\n'

        return graph

    def add_edge_between(self, start_vertex, end_vertex, edge):
        self.matrix[start_vertex][edge] += 1
        self.matrix[end_vertex][edge] += 1
        print(self.__str__())

    def remove_edge_between(self, start_vertex, end_vertex, edge):
        if self.matrix[start_vertex][edge]:
            self.matrix[start_vertex][edge] -= 1
            self.matrix[end_vertex][edge] -= 1
            print(self.__str__())
        else:
            print(f'Edge between vertices {start_vertex} and {end_vertex} does not exist')

    def exist_edge_between(self, start_vertex, end_vertex, edge):
        try:
            if self.matrix[end_vertex][edge] == 0:
                print(f'Edge between {start_vertex} and {end_vertex} does not exist')
            else:
                print('Yes')

        except IndexError:
            print('Edge or vertices does not exist')