# 맞았습니다!
# 와! 내힘으로 풀었다. 어캐 풀어야하는지 가물 가물 했는데 어찌저찌 풀렸다 신기하게도!!! 뿌듯하다

n = int(input())
dp = [0] * (n+2)
dp[0] = 0; dp[1] = 1

for i in range(2, n+1):
    dp[i] = i
    if i >= 7:
        dp[i] = min(dp[i], dp[i - 7] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + 1)
    
print(dp[n])
        
