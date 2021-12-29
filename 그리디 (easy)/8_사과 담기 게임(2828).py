'''
맞았습니다! 문제 이해가 조금 까다로웠다.
유의 해야 할 것 : 바구니 처음 시작하는 곳, 바구니 칸 수 
    스크린 N칸
    바구니 M칸
    M < N
    왼, 오 이동가능
    바구니는 스크린의 경계를 넘어가면 안됨
    아장 처음에 바구니는 왼쪽 M칸
    스크린 5칸, 바구니 1칸
    사과의 개수 3
    사과의 위치들
    1, 5, 3

'''
import sys

N, M = list(map(int, sys.stdin.readline().split()))
move, min_val, max_val = 0, 1, M

for _ in range(int(sys.stdin.readline())):
    apple = int(sys.stdin.readline())
    while True:
        print(min_val, max_val, move)
        if min_val <= apple and apple <= max_val: # 범위 안에 있으면
            break
        if apple < min_val:
            min_val -= 1; max_val -= 1
        elif apple > max_val:
            min_val += 1; max_val += 1
        move += 1
print(move)