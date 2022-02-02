# 맞았습니다!
# 점화식 어떻게 잘 찾는지 보기 ㅠ


for _ in range(int(input())):
    n = int(input())
    dp = [0] * (n+5)
    dp[1] = 1;  dp[2] = 1; dp[3] = 1; dp[4] = 2; dp[5] = 2; 

    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    
    # print(dp)
    print(dp[n])
