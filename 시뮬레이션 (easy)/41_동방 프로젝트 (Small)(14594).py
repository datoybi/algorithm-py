'''
    방의 개수 : N (2~100)
    행동 횟수 M (0~100)
    동일한 행동을 여러번 할 수 있음 
    x,y : x번방부터 y번방 사이의 벽을 무너뜨림

'''
import sys

lst = [[i] for i in range(0, int(sys.stdin.readline())+1)]

for _ in range(int(sys.stdin.readline())):
    x, y = list(map(int, sys.stdin.readline().split()))
    x_idx = 0

    for i in range(len(lst)): # x가 포함된 인덱스 찾기
        if x in lst[i]:
            x_idx = i
            break

    for j in range(x+1, y+1):
        idx = 0
        for i in range(len(lst)): # 합치기
            if j in lst[i]: 
                idx = i
                lst[x_idx].append(j)
                for z in range(len(lst[i])): # 지우기
                    if lst[i][z] == j:
                        if len(lst[i]) == 1:
                            del lst[i]
                            break
                        del lst[i][z]
                        break
                break

    # print(lst)
# print(len(lst))
print(len(lst)-1)

'''
100
6
1 9
1 8
3 10
59 60
4 70
65 95

31

10
2
6 8
1 8
'''

