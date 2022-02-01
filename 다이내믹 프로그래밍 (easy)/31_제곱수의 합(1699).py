
num = int(input())
dp = [i for i in range(num+1)]
print(dp) 

for i in range(1, num+1):
    for j in range(1, i):
        if j*j > i: # 크면 안된다 
            break
        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[num])