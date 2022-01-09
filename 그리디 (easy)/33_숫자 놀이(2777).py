'''
맞았습니다!
'''

import sys

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    i, result, check = 9, '', False

    if num < 10 : 
        print(1)
        continue

    while True:
        if num % i == 0: # 나누어 떨어지면 
            result += str(i) 
            if i < 10 and num // i < 10: # 나누어 떨어지는 숫자들이 10보다 작으면
                result += str(num // i)
                # print('ans : ' , i, num // i)
                check = True
                break
            else:
                num = num // i
                i = 9
        else: # 아무것도 아니면 
            i -= 1
            if i == 1: break

    if check == False:
        print(-1)
    else:
        print(len(result))