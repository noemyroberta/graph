from incidence_matrix import IncidenceMatrix


def main():
    matrix = IncidenceMatrix(4, 7)
    matrix.add_edge(1, 3, 0)
    matrix.add_edge(1, 2, 1)
    matrix.add_edge(1, 2, 2)

    matrix.remove_edge(1, 2, 2)
    matrix.remove_edge(1, 2, 1)

    matrix.exist_edge(1, 3, 0)

    print(matrix.exist_parallel_edges())


main()
