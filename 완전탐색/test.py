n = int(input())
t = []
p = []
dp = []


for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0) # 마지막에 0 append는 왜?!?!?!?!??

# print(t) # [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
# print(p) # [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
# print(dp) # [50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 0]

for i in range(n - 1, -1, -1): # 9 ~ 0 더 크면 0이된다. 시간이 크면 부적합하니까
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        # print(i , dp[i], dp[i + 1],  p[i] ,t[i],  dp[i + t[i]] )
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]]) # 왜 이렇게 하는 건지 노이해다..
    
    # print('dp :', dp)
print(dp[0])


# 왜 거꾸로 할까?
