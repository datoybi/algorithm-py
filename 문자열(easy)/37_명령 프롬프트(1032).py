
import sys

# 입력
N, lst = int(sys.stdin.readline()), list()

for _ in range(N):
    lst.append(sys.stdin.readline().rstrip())

answer = ''

# 계산
for i in range(len(lst[0])):
    flag = True
    tmp = lst[0][i]
    for j in range(N):
        if tmp != lst[j][i]:
            flag = False
        else:
            tmp = lst[j][i]

    if flag == True:
        answer += lst[j][i]
    else:
        answer += '?'

print(answer)