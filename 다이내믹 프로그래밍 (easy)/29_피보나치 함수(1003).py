# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    dp = [[0, 0] for _ in range(n+3)]
    dp[0] = [1, 0]; dp[1] = [0, 1]

    for i in range(2, n+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

    print(f'{dp[n][0]} {dp[n][1]}')