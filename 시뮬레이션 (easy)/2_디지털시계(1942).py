'''
맞았습니다!

    hh:mm:ss
    hh는 00 이상 23 이하
    mm과 ss는 00 이상 59 이하의 값

    시계정수 hhmmss

00:59:58 01:01:24
22:47:03 01:03:24
00:00:09 00:03:37

29
2727
70

'''

import sys
for i in range(3):
    lst = list(map(str, sys.stdin.readline().split()))

    start_h, start_m, start_s = list(map(str, lst[0].split(':')))
    end_h, end_m, end_s =list(map(str, lst[1].split(':')))

    end, start = int(end_h + end_m + end_s), int(start_h + start_m + start_s)

    if start > end : # start가 end보다 더 클때 처리
        end = int(str(int(end_h)+24) + end_m + end_s) 

    count = 0

    while True:
        if start < end:
            start = int(start_h + start_m + start_s)
            if start % 3 == 0 :
                count += 1
            # print(start_h , ':', start_m, ':',  start_s, ', ', start )
            start_s = str(int(start_s)+1)
            if len(start_s) == 1:
                start_s = '0' + start_s
        else:
            break
        
        if int(start_s) > 59:
            start_m = str(int(start_m)+1)
            if len(start_m) == 1:
                start_m = '0' + start_m
            start_s = '00'
        if int(start_m) > 59:
            start_h = str(int(start_h)+1)
            if len(start_h) == 1:
                start_h = '0' + start_h
            start_m = '00'

    print(count)