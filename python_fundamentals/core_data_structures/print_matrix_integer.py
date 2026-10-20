
#!/usr/bin/env python3
"""Print a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print each row of a matrix using format."""
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
