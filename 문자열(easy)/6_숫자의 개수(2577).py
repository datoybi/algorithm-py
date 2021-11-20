# 맞았습니다!
import sys

A, B, C = int(sys.stdin.readline()), int(sys.stdin.readline()), int(sys.stdin.readline())
value = str(A*B*C) # A,B,C를 곱한 값
zero_lst = [0 for _ in range(10)] # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in value: 
    zero_lst[int(i)] += 1

for i in zero_lst:
    print(i)