'''
# 맞았습니다!
어떻게 해야할지 감도 안잡힌다...ㅜ
https://pacific-ocean.tistory.com/197 이걸 보고 조금 이해를 해서 힌트를 얻었다.
'''
import copy

for i in range(int(input())):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(2)]
    dp = copy.deepcopy(lst)    

    for j in range(1, n):
        if j == 1:
            dp[0][1] += dp[1][0]
            dp[1][1] += dp[0][0]
        else:            
            dp[0][j] += max(dp[1][j-2], dp[1][j-1])
            dp[1][j] += max(dp[0][j-2], dp[0][j-1])  
    
    print(max(dp[0][n-1], dp[1][n-1]))