# 맞았습니다!

for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    x.insert(0,-1000)

    for i in range(2, n+1):
        x[i] = max(x[i], x[i-1] + x[i])
    
    print(max(x))

    