'''
    맞았습니다!

    n이 짝수면 2로 나눈다
    n이 홀수면 3을 곱찬뒤 1을 더한다 
    4, 2, 1, 4, 2, 1,...

    1이 나오면 수열 끝

    테케 1 <= T <= 100000
    헤일스톤 수열 n 1<= n <= 100000
'''

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    max_val = n
    while True:
        if n == 1 : 
            print(max_val)
            break    
        if n % 2 == 0:
            n = n//2
        elif n % 2 == 1:        
            n = n*3 + 1

        max_val = max(max_val, n)
