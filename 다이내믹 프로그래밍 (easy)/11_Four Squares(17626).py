'''
봤는데도 잘 모르겠다ㅜ 담에 또 풀어보기 
dp[1] = 1
dp[2] = dp[1] + 1 = 2
dp[3] = dp[2] + 1 = 3
dp[4] = dp[2*2] = 1
dp[5] = dp[4] + 1 = 2
dp[6] = dp[4] + dp[2] = 3
dp[7] = dp[4] + dp[3] = 4
dp[8] = dp[4] + dp[4] = 2

점화식 
dp[i] = dp[i - j * j] + dp[j * j]



'''
N = int(input())
dp = [0,1]

for i in range(2, N+1):
    min_value = 1e9
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1

    dp.append(min_value + 1)
print(dp[N])

print(dp)