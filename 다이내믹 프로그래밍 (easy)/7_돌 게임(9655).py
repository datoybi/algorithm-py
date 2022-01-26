# 맞았습니다!
# 뭔가 dp로 안푼 느낌.. 담에 다시 풀어봐야겠다
import sys

N = int(sys.stdin.readline())
dp = [1001] * (N+4)
dp[1] = 0; dp[2] = 1; dp[3] = 0;
print(dp)

for i in range(4, N+1):
    if dp[i-1] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

print(dp)
print('SK' if dp[N] == 0 else 'CY')
