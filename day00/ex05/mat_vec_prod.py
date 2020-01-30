#!/usr/local/bin/python3

import numpy as n

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

def mat_vec_prod(x:n.ndarray, y:n.ndarray):
    result = n.ndarray(shape=(x.shape[0], y.shape[1]))
    if not (len(x) and len(y)) or x.shape[1] - y.shape[0]:
        print("Input error : x and y should be non-empty compatible ndarrayas ")
        return None
    for i, row in enumerate(x):
        result[i] = dot(row, y)
    return result

# x = n.array([[0, 1], [2, 3], [4, 5]]).reshape(3, 2)
# y = n.array([[6], [7]]).reshape(2,1)
# mat_vec_prod(x, y)

# W = n.array([
#     [ -8, 8, -6, 14, 14, -9, -4],
#     [ 2, -11, -2, -11, 14, -2, 14],
#     [-13, -2, -5, 3, -8, -4, 13],
#     [ 2, 13, -14, -15, -14, -15, 13],
#     [ 2, -1, 12, 3, -7, -3, -6]])

# X = n.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))
# Y = n.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))
# print(mat_vec_prod(W, Y))
# print(W.dot(Y))

