
#!/usr/bin/env python3
"""Function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers using format."""
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))

