'''
맞았습니다!
5 3 
18 -> 5 3, 3 1
4 -> -1
6 -> 2
9 -> 3
11 -> 5 1 3 2 
'''
N = int(input())
cnt, flag = N, False

for i in range((N//5)+1):
    for j in range((N//3)+1):
        if i*5 + j*3 == N:
            cnt = min(cnt, i+j)
            flag = True

print(-1 if flag == False else cnt)