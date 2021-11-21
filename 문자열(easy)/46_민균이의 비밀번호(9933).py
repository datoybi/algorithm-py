# 맞았습니다!
import sys

# list에 단어 삽입
lst = list()
for i in range(int(sys.stdin.readline())):
    lst.append(sys.stdin.readline().rstrip())

# print(lst)

for i in range(len(lst)):
    tmp = lst[i]
    if tmp[::-1] in lst: # 단어를 뒤집은게 lst 안에 있으면
        print(len(tmp), tmp[int(len(tmp)/2)])
        exit(0)