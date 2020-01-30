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
    print(f'{x.shape[0]},{y.shape[1]}')
    result = n.ndarray(shape=(x.shape[0], y.shape[1]))
    # print(f'mat_mat | mat_vec | resullt[{x.shape[0]}][{y.shape[1]}]')
    if not (len(x) and len(y)) or x.shape[1] - y.shape[0]:
        print("Input error : x and y should be non-empty compatible ndarrayas ")
        return None
    for i, row in enumerate(x):
        result[i] = dot(row, y)
    return result

def mat_mat_prod(x:n.ndarray, y:n.ndarray):
    result = n.ndarray(shape=(x.shape[0], y.shape[1]))
    # print(f'[{x.shape[0]}][{y.shape[1]}]')
    if not (len(x) and len(y)) or x.shape[1] - y.shape[0]:
        print("Input error : x and y should be non-empty compatible ndarrayas ")
        return None
    for i, row in enumerate(x):
        for j in range(0, y.shape[1] - 1) :
            result[i][j] = dot(row, y[:,j])
    return result
    #===========
    #     result[i] = mat_vec_prod(row, y[:, i])#// doesnt work cause mat_vec_prod expects y to be
    # print(dot(x, y[:, 0]))
    # for i, row in enumerate(x):
    #     for j, value in enumerate(y):
    #     col = y[j]
    #     result[i, j]
    # print(y[:,0])
    # vect = mat_vec_prod(x[0], y[:,0])
    # result[0][1]= dot(x[0], y[:,1])
    # print(result[0][0])
    # for j in range(0, y.shape[1]):
    # result[:,0] =  mat_vec_prod(x, y[:,0])
    # result[:,0] = y[:, 0]
    # print(f'result[{result.shape[0]}][{result.shape[1]}]')
    print(mat_vec_prod(x, y[:,0]))
    # for row in x:
    #     print(dot(row, y[:,0]))
    
W = n.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])
Z = n.array([
    [ -6, -1, -8, 7, -8],
        [ 7, 4, 0, -10, -10],
        [ 7, -13, 2, 2, -11],
        [ 3, 14, 7, 7, -4],
        [ -1, -3, -8, -4, -14],
        [ 9, -14, 9, 12, -7],
        [ -9, -4, -10, -3, 6]])

# mat_mat_prod(W, Z)
# print(mat_mat_prod(W, Z))
mat_mat_prod(W, Z)