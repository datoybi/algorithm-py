'''
맞았습니다!
'''

test_case, M = map(int,input().split(' '))
N = list(map(int, input().split(' ')))
max = 0

for i in range(0, len(N)):
    for j in range(i+1, len(N)):
        for z in range(j+1, len(N)):
            # print(N[i], N[j], N[z])
            temp = N[i] + N[j] + N[z]
            if temp <= M :
                if abs(M-max) > abs(M-temp):
                    max = temp

print(max)






