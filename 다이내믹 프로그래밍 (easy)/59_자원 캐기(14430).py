'''
맞았습니다!
오른쪽, 아래쪽으로 한 칸
'''
n, m = list(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = lst[0][0]
        elif i == 0:
            dp[i][j] = dp[i][j-1] + lst[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + lst[i][j]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + lst[i][j]

print(dp[n-1][m-1])
