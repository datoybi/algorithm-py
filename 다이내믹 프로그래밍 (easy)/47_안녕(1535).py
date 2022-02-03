# 점화식을 못찾겠어! 담에 풀어보기
'''
베낭문제이다.. 다음에 다시 한번 보자
각 가방의 가치 : v[n]
각 가방의 무게 : w[n]
최대이윤 : dp[m][n]이라 할 때,
(w[i] <= j ) dp[i][j] = max(v[i] + dp[i-1][j - w[i]], dp[i-1][j]
(w[i] > j) dp[i][j] = dp[i-1][j]
'''

N = int(input())
L = [int(x) for x in input().split()] 
J = [int(x) for x in input().split()] 
L, J = [0] + L, [0] + J 
dp = [[0 for _ in range(101)] for _ in range(N+1)] 

for i in range(1, N+1): 
    for j in range(1, 101): 
        if L[i] <= j: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - L[i]] + J[i]) 
        else: 
            dp[i][j] = dp[i-1][j] 
print(dp[N][99])


'''
n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
d=[0 for _ in range(101)]

for i in range(n):
    for j in range(99, a[i]-1,-1):
        d[j]=max(d[j], d[j - a[i]] + b[i])

print(max(d))

'''

