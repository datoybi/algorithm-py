# 정해진 최선의 연산 방법이 없기 때문에 다 시도해보아야 한다.라는 점을 방금 생각했었는데 놓쳤었다. 
# 그래도 점화식을 비슷하게 잘 찾았다 잘했다 솜 !
# 맞았습니다!

n = int(input())
dp = [0] * (n+3)
dp[1] = 0; dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1) 
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
        
print(dp)
print(dp[n])


# n = int(input())
# dp = [0] * (n+3)
# dp[1] = 0; dp[2] = 1

# for i in range(3, n+1):
#     if i % 3 == 0:
#         dp[i] = min(dp[i-1], dp[i//3]) + 1
#     elif i % 2 == 0:
#         dp[i] = min(dp[i-1], dp[i//2]) + 1
#     else:
#         dp[i] = dp[i-1] + 1
        
# print(dp)
# print(dp[n])
