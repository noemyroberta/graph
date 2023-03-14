from incidence_matrix import IncidenceMatrix


def main():
    matrix = IncidenceMatrix(4, 7)
    matrix.add_edge_between(1, 3, 0)
    matrix.add_edge_between(3, 3, 1)
    matrix.add_edge_between(3, 3, 2)
    matrix.remove_edge_between(1, 3, 0)
    matrix.remove_edge_between(2, 3, 1)

    print(matrix.exist_edge_between(4, 4, 0))


main()
