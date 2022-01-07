'''
맞았습니다!
N 
N-2 번

7 6 9
len이 3개남았을때는 다 삭제 
남은 두 폭죽 더미의 높이 중 더 큰 값을 최소화하려고 합니다.

'''
import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

while True:
    if len(lst) > 3: # 길이가 3보다크면 큰수에 -1
        del lst[len(lst)//2]
        if lst[0] > lst[-1]:
            lst[0] -= 1
        else:
             lst[-1] -= 1
    else: # 길이가 3이면 양 끝 둘다 -1
        del lst[1]
        lst[0] = lst[0]-1
        lst[-1] = lst[-1]-1
        break

print(max(lst[0], lst[-1]))
    

# 부분점수 31점
# import sys
# N = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# print(max(lst[0], lst[-1]) - (N-2))
