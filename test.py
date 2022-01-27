R, C, W = map(int, input().split())
tri = [[0] * 31 for _ in range(31)]
for i in range(len(tri)):
    tri[0][i] = 1
for i in range(len(tri)):
    for j in range(i + 1):
        if j == 0:
            tri[i][j] = 1
        elif j == i:
            tri[i][j] = 1
        else:
            tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]
 
S, cnt = 0, 0
for i in range(R - 1, R + W - 1):
    for j in range(C - 1, C + cnt):
        S += tri[i][j]
    cnt += 1
print(S)

