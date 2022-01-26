# 맞았습니다!
# 대충은 알것같긴 한뎅...ㅜㅜ 좀 어렵다 이논리가 왜 맞는지는 잘 모르겠당..
# 당최 dp로 어캐 접근하는지 감이 안잡힌다.

import sys

N = int(sys.stdin.readline())
dp = [100000001] * (N+5)
dp[2] = 1; dp[4] = 2; dp[5] = 1

for i in range(6, N+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1
    
print(dp[N] if dp[N] < 100000000 else -1)