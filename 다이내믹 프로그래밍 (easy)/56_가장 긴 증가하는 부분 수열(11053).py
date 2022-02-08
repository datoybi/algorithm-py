'''
# 맞았습니다!
얼추 비슷하게 구현하긴 했는데 tmp를 만들어서 카운트를 하는 대신 DP를 이용해서 
하는 방법이 어려웠다. 다음에 또 풀어보기 ㅜ
'''

n = int(input())
lst = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):       
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

