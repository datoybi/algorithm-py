# 봐도 모르겠당 ㅠㅜ
import sys

N = int(sys.stdin.readline())
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 0
lst = list()
for i in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    lst.append([a, b, c, d])
print(lst)    
print(dp)

for i in range(N):
    for j in range(N):
        if i + lst[i][j] > N: 
            continue
        else:
           dp[i + lst[i][j]][j] = min(dp[i + lst[i][j]][j], dp[i + lst[i][j]][j] + 1)
        if j + lst[i][j] > N: 
            continue
        else:
            dp[i][j + lst[i][j]] = min(dp[i][j + lst[i][j]], dp[i][j + lst[i][j]] + 1)
        print(dp)

print(dp)
        