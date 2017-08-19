#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import argparse
import sys


def fib1(n):
    """ Recursive Fibonacci """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    """ Faster Fibonacci """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


parser = argparse.ArgumentParser(description="Calculate the n-th value of the \
                                Fibonacci sequence")
parser.add_argument("infile", nargs="?", default=sys.stdin,
                    type=argparse.FileType("r", encoding="utf-8"),
                    help="the file with the input data")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

n = int(args.infile.read())
args.infile.close()

fibonacci = fib2(n)

with open("output/fibo.txt", "w", encoding="utf-8", newline="\n") as outfile:
    outfile.write(str(fibonacci) + "\n")

if args.verbose:
    print("The value of F({}) is ".format(n), end="")
print(fibonacci)
