# 맞았습니다!
import sys

for _ in range(int(sys.stdin.readline())):
    A, B = map(str, sys.stdin.readline().split())
    lst = [0 for _ in range(123)]

    for i in A: # A의 값만큼 넣기 
        lst[ord(i)] += 1
    
    for i in B: # B의 값만큼 빼기 
        lst[ord(i)] -= 1

    flag = True

    for i in lst:
        if i != 0: # 원소가 양수면 A가 다 삭제되지 못함-> A가 에너그램이 아님
            flag = False
            break

    print(f'{A} & {B} are anagrams.' if flag == True else f'{A} & {B} are NOT anagrams.')
