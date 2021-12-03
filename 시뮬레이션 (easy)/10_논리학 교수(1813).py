'''
맞았습니다!

아니 문제이해를 못해서 못푼 문제다.. 이 한줄로 이해가 깔끔하게 됐다.
!!!!!!"n개의 말이 참이다." 가 전체 N개 중에 n개만큼 존재하면 n개의 말이 참이 된다.!!!!!!1

말의 개수 N
입력값

0개의 말은 참이다.
1개의 말은 참이다.
2개의 말은 참이다.
3개의 말은 참이다.
 
답 1

문제를 이해 못하겠다
'''
import sys

result = -1
N = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))
zero_lst = [ 0 for _ in range(0, 51)]

for i in range(len(n_lst)):
    zero_lst[n_lst[i]] += 1

for i in range(len(zero_lst)):
    if zero_lst[i] == i:
        result = max(result, i)

print(result)