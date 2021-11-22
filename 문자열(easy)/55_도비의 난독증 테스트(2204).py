# 맞았습니다!
import sys

while True:
    N, lst, copy_lst = int(sys.stdin.readline()), list(), list()
    if N == 0: exit(0) # 0이면 나가기 

    for _ in range(N):
        tmp = sys.stdin.readline().rstrip()
        lst.append(tmp)
        copy_lst.append(tmp.lower())
    
    copy_lst.sort()
    # print(copy_lst[0])

    for i in range(len(lst)):
        if lst[i].lower() == copy_lst[0]:
            print(lst[i])


