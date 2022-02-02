'''
어렵당
끝나는 수를 생각해서 규칙을 찾아야 할 줄 몰랐다.
담에 다시 해보기 ㅠ 강의듣고..
'''

n = int(input())
dp = [0] * (n+2)
dp[0] = 0; dp[1] = 1; dp[2] = 1;

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]


print(dp)
print(dp[n])