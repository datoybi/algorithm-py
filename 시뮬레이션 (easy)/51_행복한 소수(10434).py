'''
맞았습니다!

자리수의 제곱의 합을 구하는 연산을 반복했을 때 1이 되는 수
1은 소수가 아니다

'''

import sys

for _ in range(int(sys.stdin.readline())):
    N, M = list(map(int, sys.stdin.readline().split()))
    num, answer, count = str(M), 'NO', 0

    if M != 1:
        while count != 1000: # 행복한지 판별 카운트가 1000이상일때는 NO
            if num == '1':
                answer = 'YES'
                break
            total = 0
            for i in range(len(num)):
                total += int(num[i])*int(num[i]) # 연산
            if total != num:
                num = str(total)
                count += 1
        if answer == 'YES': # 소수인지 판별
            for i in range(M-1, 1, -1):
                if M % i == 0: # 나누어떨어지는게 있으면 소수가 아님
                    answer = 'NO'
                    break

    print(N, M, answer)