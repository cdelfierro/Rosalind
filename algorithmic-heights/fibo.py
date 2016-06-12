#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock

"""
Recursive fibonacci
"""
def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)

"""
Faster fibonacci
"""
def fib2(n):
    if n == 0:
        return 0
    f = [None] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

try:
    x = int(sys.argv[1])
except ValueError:
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
            x = int(ini_file.read().strip())
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
except:
    x = int(sys.stdin.read())

start = clock()
fibonacci = fib2(x)
end = clock()
time = end - start

with open("output/fibo.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(str(fibonacci) + "\n")

print(fibonacci)
print("Time: {} segs.".format(time))
