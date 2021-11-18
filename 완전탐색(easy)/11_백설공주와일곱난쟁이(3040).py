'''
맞았습니다!
'''

N, t1, t2 = list(), 0, 0
for _ in range(0,9) :
    N.append(int(input()))

for i in range(0, 9):
    for j in range(i+1, 9): 
        if (sum(N[0:]) - N[i] - N[j]) == 100:
            t1, t2 = N[i] ,N[j]
            
N.remove(t1)
N.remove(t2)

for i in N:
    print(i)