# 맞았습니다!
# 풀었는데 왜 틀렸는지 모르겠다 ㅜㅜㅜ 담에 또 풀어보기 ...

n = int(input())
data = list(map(int, input().split()))

for i in range(1, n):
  data[i] = max(data[i], data[i] + data[i-1])

print(max(data))

# n = int(input())
# lst = list(map(int, input().split()))
# lst.insert(0,-999999)
# dp = [-999999] * (n+1)
# dp[1] = value = lst[1]

# for i in range(2, n+1):
#     print(i, value)
#     if lst[i] <= 0:
#         if dp[i-1] + lst[i] > 0:
#             value += lst[i]
#             dp[i] = value
#         else:
#             value = 0
#             dp[i] = max(dp[i-1], lst[i])
#     else:
#         value += lst[i]
#         dp[i] = max(dp[i-1], value, lst[i])

#     print(dp)
# print(dp[n])
