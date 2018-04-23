#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import argparse
import sys
from sequences import linear_fib as F


parser = argparse.ArgumentParser(description="Calculate the n-th value of the \
                                Fibonacci sequence")
parser.add_argument("infile", nargs="?", default=sys.stdin,
                    type=argparse.FileType("r", encoding="utf-8"),
                    help="the file with the input data")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

n = int(args.infile.read())
args.infile.close()

fibonacci = F(n)

with open("output/fibo.txt", "w", encoding="utf-8", newline="\n") as outfile:
    outfile.write(str(fibonacci) + "\n")

if args.verbose:
    print("The value of F({}) is ".format(n), end="")
print(fibonacci)
