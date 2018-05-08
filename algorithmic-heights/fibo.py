#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import argparse
from sequences import linear_fib as F


def main():
    """Calculate the n-th value of the Fibonacci sequence"""
    parser = argparse.ArgumentParser(
        prog='fibo',
        description='Calculate the n-th value of the Fibonacci sequence')
    group = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument('-v', '--verbose', action='store_true')
    group.add_argument(
        '-i', '--infile', type=argparse.FileType('r', encoding='utf-8'),
        help='the file with the input data')
    group.add_argument('-n', type=int, help='the n-th value of the Fibonacci sequence to calculate')
    parser.add_argument(
        '-o', '--outfile', type=argparse.FileType('w', encoding='utf-8'),
        help='the file with the output data')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()

    if args.n:
        n = args.n
    elif args.infile:
        n = int(args.infile.read())
        args.infile.close()

    fibonacci = F(n)

    if args.outfile:
        args.outfile.write(str(fibonacci) + '\n')
        args.outfile.close()
    else:
        with open('output/fibo.txt', 'w', encoding='utf-8', newline='\n') as outfile:
            outfile.write(str(fibonacci) + "\n")

    if args.verbose:
        print('The value of F({}) is '.format(n), end='')
    print(fibonacci)


if __name__ == '__main__':
    main()
