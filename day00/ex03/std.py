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

def variance(x):
    sum = 0
    m = mean(x)

    for i in x:
        sum += (i - m) ** 2
    return (sum / len(x))

