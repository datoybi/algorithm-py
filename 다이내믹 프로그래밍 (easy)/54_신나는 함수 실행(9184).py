# 맞았습니다!
'''
dp[1][1][21] 일때 값이 구해져있지 않았다는걸 몰랐다 ㅠㅠ 왜 거기까지 생각이 안미치는건지 에효효
'''

dp = [[[0 for _ in range(51)] for j in range(51)] for _ in range(51)]

for i in range(0, 51):
    for j in range(0, 51):
        for z in range(0, 51):
            if i <= 0 or j <= 0 or z <= 0:
                dp[i][j][z] = 1
                continue
            if i > 20 or j > 20 or z > 20:
                # dp[i][j][z] = dp[20][20][20] # dp[1][1][21] 일때 값이 구해져있지 않음
                dp[i][j][z] = 1048576
                continue
            if i < j and j < z:
                dp[i][j][z] =  dp[i][j][z-1] + dp[i][j-1][z-1] - dp[i][j-1][z]
            else:
                dp[i][j][z] = dp[i-1][j][z] + dp[i-1][j-1][z] + dp[i-1][j][z-1] - dp[i-1][j-1][z-1]

while True:
    A, B, C = map(int, input().split()) 
    a = A; b = B; c = C
    if a == -1 and b == -1 and c == -1 : break
    if A <= 0: a = 0
    if B <= 0: b = 0
    if C <= 0: c = 0
    print(f'w({A}, {B}, {C}) = {dp[a][b][c]}')