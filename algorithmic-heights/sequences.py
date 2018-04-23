#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""


def recursive_fib(n):
    """ Recursive Fibonacci """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def linear_fib(n):
    """ Linear Fibonacci """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
