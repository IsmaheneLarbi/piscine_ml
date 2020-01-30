#!/usr/local/bin/python3

import numpy as n
import types as t
from inspect import signature

def sum_(x:n.ndarray, f):
    """
    x   takes an ndarray as a param,
    x   applies f to each element of vector x
    x   does the sum of the results
    x   returns it in a float
        checks whether f is a valid function without throwing any exceptions/errors
    """
    sum = 0
    sign = signature(f)
    print(sign.parameters)

    if not len(x) or not isinstance(f, t.FunctionType) or len(sign.parameters) != 1:
        print("Input error: x has to be of type numpy.ndarray and f has to be a valid function")
        return None
    for i in x:
        sum += f(i)
    return float(sum)

def mean(x:n.ndarray):
    sum = 0

    if not len(x):
        print("Input error: x has to be of type numpy.ndarray and f has to be a valid function")
        return None  
    sum = sum_(x, lambda x:x)
    return (sum / len(x))

def mse(y:n.ndarray, y_hat:n.ndarray):
    mse = n.ndarray(shape=y.shape)

    if not (y.shape[0] and y_hat.shape[0]) or (y.shape[0] - y_hat.shape[0]):
        print("Input error : x and y should be non-empty ndarrayas of the same size")
        return None
    for i, elt in enumerate(mse):
        mse[i] = (y_hat[i] - y[i]) ** 2
        # print(f'{mse[i]} = ({y_hat[i]} - {y[i]}) ** 2')
    return mean(mse)

# X = n.array([0, 15, -9, 7, 12, 3, -21])
# Y = n.array([2, 14, -13, 5, 12, 4, -19])
# # mse(X, Y)
# print(mse(X, Y))