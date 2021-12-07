
import sys
ruler = int(sys.stdin.readline())

for _ in range(3):
    start, end = list(map(int, sys.stdin.readline().split()))
    half = (start+end)/2

    print(half)