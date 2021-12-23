# 맞았습니다!
import sys

count = 0
while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == '문제':
        count += 1
    elif sentence =='고무오리' and count <= 0:
        count += 2
    elif sentence =='고무오리' and count > 0:
        count -= 1
    elif sentence =='고무오리 디버깅 끝':
        break

if count == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')

    