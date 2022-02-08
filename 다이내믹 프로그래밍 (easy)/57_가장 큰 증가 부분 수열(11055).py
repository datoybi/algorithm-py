'''
# 맞았습니다!
반례 모음집
https://joey09.tistory.com/108

'''

import copy

n = int(input())
lst = list(map(int, input().split()))
# dp = [1 for _ in range(n)] # 정확히 이것이 왜 필요하지 않는지는 설명하기 힘들다 ...
# dp[0] = lst[0]
dp = copy.deepcopy(lst)

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[j] + lst[i], dp[i])
print(max(dp))
