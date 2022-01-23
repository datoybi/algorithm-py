import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
count = 0

# 알고리즘
for j in range(len(coins) - 1, -1, -1):
    if K // coins[j] == 0:
        continue
    else:
        coin_count = K // coins[j]
        count += coin_count
        K %= coins[j]

print(count)
