'''
이거.. LIS 라는 알고리즘 이란다.. 나중에 한번 더 풀어보자
'''
n = int(input())
lst = list(map(int,input().split()))
dp = [1] * 1001

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)    
print(max(dp))



# 왜 이건 안되는 건데?? 나중에라도 알ㄷ게된다면.. 좋겟다^^
# n = int(input())
# lst = list(map(int,input().split()))
# lst.insert(0, 0)
# dp = [1] * (n+1)

# for i in range(1, n+1):
#     for j in range(i+1, n+1):
#         if lst[i] < lst[j]:
#             dp[j] = max(dp[j], dp[i]+1)

# print(dp)    
# print(dp[n])