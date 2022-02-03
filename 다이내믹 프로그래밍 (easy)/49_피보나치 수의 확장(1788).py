'''
맞았습니다!
홀.. 너무 곧이 곧대로 좀 어렵게생각했었다
dp(-1) = dp(1) - dp(0) 이 공식을 찾았었는데 이것보다 그냥 짝수 개는 음수였다.

'''
n = int(input())

if n == 0:
    print('0\n0')
    exit(0)

dp = [0] * (abs(n)+3)
dp[0] = 0; dp[1] = dp[2] = 1

for i in range(3, abs(n)+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 1000000000
    
if n < 0 and abs(n) % 2 == 0:
    print(-1)
else:
    print(1)
print(abs(dp[abs(n)]) % 1000000000)



# n = int(input())

# dp = [0] * (abs(n)+2)
# dp[0] = 0; dp[1] = 1
# flag = 1
# if n < 0 :
#     flag = -1
#     dp[2] = -1

# for i in range(2, abs(n)+1):
#     if flag == -1: 
#         dp[i] = (dp[i-2] - dp[i-1]) % 1000000000
#     else:
#         dp[i] = (dp[i-2] + dp[i-1]) % 1000000000

# if dp[abs(n)] == 0:
#     print(0)
# elif dp[abs(n)] > 0:
#     print(1)
# else:
#     print(-1)

# print(abs(dp[abs(n)]) % 1000000000)