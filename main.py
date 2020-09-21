#!/usr/bin/python3

"""
Author: Wecros (Marek Filip)

Description: Compute the pi number from the probability of Buffon's needle problem.

Args:
    -l: length of the needle
    -d: distance between two lines
    -n: number of tries
"""
import sys
import math
from random import uniform

PI = math.pi


def compute_pi(l: float, d: float, n: int, m: int) -> float:
    return (2 * l * n) / (d * m)

def compute_m(l: float, d: float, n: int) -> int:
    m = 0
    for _ in range(n):
        phi = uniform(0, PI / 2)
        x = uniform(0, d / 2)
        y = (l / 2) * math.sin(phi)

        if (x <= y):
            m += 1

    return m


def main():
    l = float(sys.argv[1])
    d = float(sys.argv[2])
    n = int(sys.argv[3])

    m = compute_m(l, d, n)

    print(compute_pi(l, d, n, m))


if __name__ == "__main__":
    main()
