# 맞았습니다!

for _ in range(int(input())):
    n = int(input())
    koong = [0] * (n+4)
    koong[0] = 1; koong[1] = 1; koong[2] = 2; koong[3] = 4

    for i in range(4, n+1):
        koong[i] = koong[i-1] + koong[i-2] + koong[i-3] + koong[i-4]    
        
    print(koong[n])