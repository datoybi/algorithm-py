'''
1. 수의 합을 반복적으로 구합니다.
2. 이 때 합이 음수이면 그 다음 수부터 다시 시작합니다.
3. 합의 최댓값을 도출합니다.

'''
n = 10
lst = [-3, 3, 5, -3, -7, 9, -2, 10, -5, -2]
dp = [0 for _ in range(n)]
if lst[0] > 0:
    dp[0] = lst[0]

for i in range(1, n):
    dp[i] = dp[i-1] + lst[i]
    if dp[i] < 0:
        dp[i] = 0

if max(lst) < 0 :
    print(max(lst))
else:
    print(max(dp))