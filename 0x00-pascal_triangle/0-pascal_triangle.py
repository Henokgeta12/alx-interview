#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    """
    pascaltriangle
    """
    triangle = []
    for i in range(1, n + 1):
        row = []
        c = 1
        row.append(c)
        for j in range(1, i):
            # Calculate the next value based on the previous row
            c = c * (i - j) // j
            row.append(c)
        triangle.append(row)
    return triangle
