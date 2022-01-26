'''
맞았습니다! 
dp로 처음 풀어보았다. 나름 잘 되네 !??
    A만 표시되어져 있다. 버튼을 누르니 글자가 B로 변했다. 
    한번더 누르니 BA
    그다음엔 BAB
    그리고 BABBA 


'''

import sys

N = int(sys.stdin.readline())
dp = [[0, 0] for _ in range(46)]
dp[0] = [1, 0]; dp[1] = [0, 1]

for i in range(2, N+1):
    if dp[i]:
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

# print(dp)
print(f"{dp[N][0]} {dp[N][1]}")


# 메모리 초과
# import sys

# N = int(sys.stdin.readline())
# dp = ['0' for _ in range(46)]
# dp[0] = 'A'; dp[1] = 'B'

# for i in range(2, N+1):
#     if dp[i]:
#         dp[i] = dp[i-1] + dp[i-2]

# print(dp)
# print(f"{dp[N].count('A')} {dp[N].count('B')}")