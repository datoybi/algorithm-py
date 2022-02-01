'''
맞았습니다!
규칙 찾을 때 꼼꼼하게 잘 찾기!!!!! 괜히 이상하게 찾아서 규칙 못찾아서 틀리는 경우가 생긴다.
'''

for _ in range(int(input())):
    n = int(input())
    dp = [0] * 11
    dp[1] = 1; dp[2] = 2; dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[n])
    