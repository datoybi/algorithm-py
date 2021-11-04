from itertools import permutations
import sys
input = sys.stdin.readline

n,k = int(input()), int(input())
cards = [input().rstrip() for _ in range(n)]
res = set()

for per in permutations(cards, k):
    res.add(''.join(per))

print(res)
print(len(res))
