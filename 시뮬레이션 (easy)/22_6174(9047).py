'''
맞았습니다!

1000으로 시작하면 999만 남아서 계속 시간초과가 떴었다.
반례 
1
0999
1
1000

'''

import sys

count = 0

for _ in range(int(sys.stdin.readline())):
    num = sys.stdin.readline().rstrip()
    count = 0

    while True:
        str_num = list(str(num))
        if str_num == ['6', '1', '7', '4']:
            break
        if len(str_num) != 4:
            while len(str_num) !=4:
                str_num.append('0')

        max_val, min_val ='', ''

        str_num.sort() # 최대값
        print(str_num)
        for i in str_num:
            min_val += i

        str_num.reverse() # 최소값
        print(str_num)
        for i in str_num:
            max_val += i

        print(max_val, min_val)
        num = int(max_val)-int(min_val)
      
        count += 1

    print(count)
    


