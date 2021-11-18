'''
맞았습니다!

'''
X, Y, P1, P2 = map(int, input().split())
A, B = list(), list()

for i in range(100):
    A.append(P1+X*i)
    B.append(P2+Y*i)

for j in A :
    if j in B:
        print(j)
        exit(0)

print(-1)

