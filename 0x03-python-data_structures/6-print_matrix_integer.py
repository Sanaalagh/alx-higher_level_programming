#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for inmatrix in matrix:
        if len(inmatrix) == 0:
            print()
        for i in range(len(inmatrinx)):
            print("{:d}".format(inmatrix[i]),end ="\n" if i is len(inmatrix) - 1 else " ")
