'''
맞았습니다!
R 번쨰 줄 
C: 1번째 수 
W: 4개의 수 포함(변)
'''

import sys

R, C, W = list(map(int, sys.stdin.readline().split()))
dp = [[1]]
for i in range(1, R+W): # dp setting
    tmp = []
    for j in range(1, i+1):
        tmp.append(1)
    dp.append(tmp)

for i in range(3, R+W): 
    for j in range(1, i-1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

result = 0
c = C
for i in range(R, R+W): 
    # print(i, j) 
    print(dp[i][C-1:c])
    result += sum(dp[i][C-1:c])
    c += 1

print(result)

  