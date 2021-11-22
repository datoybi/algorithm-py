
import sys

set_lst = set()
for _ in range(int(sys.stdin.readline())):
    set_lst.add(sys.stdin.readline().rstrip())
lst, answer = list(set_lst), list()
# 맞았습니다!
'''
반례
1
a 
'''
for i in range(1, 51): # 문자 50개까지 가능
    tmp = list()
    for j in range(len(lst)):
        if len(lst[j]) == i:
            tmp.append(lst[j])
    tmp.sort()
    for j in tmp:
        answer.append(j)

for i in answer:
    print(i)
