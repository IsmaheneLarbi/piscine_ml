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

def mse_vec(y:n.ndarray, y_hat:n.ndarray):
    mse_vec = n.ndarray(shape=y.shape)

    mse_vec = (y_hat - y) ** 2
    return (mean(mse_vec))


X = n.array([0, 15, -9, 7, 12, 3, -21])
Y = n.array([2, 14, -13, 5, 12, 4, -19])

print(mse_vec(X, Y))