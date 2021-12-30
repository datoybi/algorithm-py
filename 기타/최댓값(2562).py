# 맞았습니다!
m = [0, 0]
for i in range(9):
    a = int(input())
    m[0] = max(a, m[0])
    if a == m[0]:
        m[1] = i+1

print(m[0]); print(m[1])
