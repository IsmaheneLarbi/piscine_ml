#!/usr/local/bin/python3

import numpy as n

def dot(x:n.ndarray, y:n.ndarray):
    """
    calculates the angle between two vectors:
    how much are they pointing at the same direction ?
    r.s = |r| . |s| cos O, if O = 0 => cos O =1 => r.s = |r| . |s| // same direction
                            if O = 90 => cos O = 0 => r.s = 0 // orthogonal vectors
                            if O = 180 => cos O = -1 => r.s = -|r| .|s|
    """
    dot = 0

    if not (len(x) and len(y)) or (len(x) - len(y)):
        print("Input error : x and y should be non-empty ndarrayas of the same size")
        return None
    for i, elt in enumerate(x):
        dot += elt * y[i]
    return (float(dot))

X = n.array([0, 15, -9, 7, 12, 3, -21])
Y = n.array([2, 14, -13, 5, 12, 4, -19])
print(dot(X, Y))
# print(dot(X, X))
# print(dot(Y, Y))