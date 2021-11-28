# n! / k!(n-k)!

import sys
from math import factorial

n1, n2 = map(int, sys.stdin.readline().split())
b = factorial(n1) // (factorial(n2) * factorial(n1-n2))
print(b)

