'''
맞았습니다!
0.25
0.10
0.05
0.01

거스름돈은 항상 $5.00 이하
동전 최소


'''
import sys

for _ in range(int(sys.stdin.readline())):
    C = int(sys.stdin.readline())
    print(C // 25, C % 25 // 10, C % 25 % 10 // 5, C % 25 % 10 % 5 // 1 )