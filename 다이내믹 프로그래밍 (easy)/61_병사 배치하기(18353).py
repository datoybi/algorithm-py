# 맞았습니다!

n = int(input())
lst = list(map(int, input().split()))
dp = [1 for _ in range(n+1)]

for i in range(1, n):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
