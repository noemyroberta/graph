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

    def add_edge(self, start_vertex, end_vertex, edge):
        self.matrix[start_vertex][edge] += 1
        self.matrix[end_vertex][edge] += 1
        print('Add edge')
        print(self.__str__())

    def remove_edge(self, start_vertex, end_vertex, edge):
        if self.matrix[start_vertex][edge]:
            self.matrix[start_vertex][edge] -= 1
            self.matrix[end_vertex][edge] -= 1
            print('Removing edge')
            print(self.__str__())
        else:
            print(f'Edge between vertices {start_vertex} and {end_vertex} does not exist')

    def exist_edge(self, start_vertex, end_vertex, edge):
        try:
            if self.matrix[end_vertex][edge] == 0 or self.matrix[start_vertex][edge] == 0:
                print(f'Edge between {start_vertex} and {end_vertex} does not exist')
            else:
                print('Yes, exist an edge between')

        except IndexError:
            print('Edge or vertices does not exist')

    def get_number_of_edges(self, start_vertex, end_vertex):
        edges = 0

        for edge in range(self.edges_size):
            if self.matrix[start_vertex][edge] > 0 and self.matrix[end_vertex][edge] > 0:
                edges += 1

        return edges

    def exist_parallel_edges(self):
        for start_vertex in range(self.vertices_size):
            for end_vertex in range(self.vertices_size):
                if self.get_number_of_edges(start_vertex, end_vertex) > 1:
                    return True
        return False
