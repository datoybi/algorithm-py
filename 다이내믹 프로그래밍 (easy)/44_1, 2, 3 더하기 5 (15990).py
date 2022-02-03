'''
어렵당
끝나는 수를 생각해서 규칙을 찾아야 할 줄 몰랐다.
뭔가 연관된 규칙성을 찾는게 어렵당ㅠ
'''

dp = [[0 for _ in range(3)] for _ in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

for _ in range(int(input())): 
    n = int(input()) 
    print(sum(dp[n]) % 1000000009)
        
