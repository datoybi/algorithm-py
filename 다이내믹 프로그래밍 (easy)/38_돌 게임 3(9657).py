# 솔직히 규칙 조차 잘 못찾겠다 
# 패승패 승승승승 어떻게 나오는지도 헷갈리고.. 찾아보려 했는데도!@#
# 담에 또 풀어보기

n = int(input())
dp = [0] * 1001
dp[1] = 1; dp[3] = 1; dp[4] = 1;

if n >= 5:
    for i in range(5, n+1): 
        if not dp[i-1]:
            dp[i] = 1
        if not dp[i-3]:
            dp[i] = 1
        if not dp[i-4]:
            dp[i] = 1

print(dp)
if dp[n]:
    print("SK")
else:
    print("CY")




'''
1	SK
2	CY
3	SK
4	SK
5	SK
6	SK
7	CY
8	SK
9	CY
10	SK
'''