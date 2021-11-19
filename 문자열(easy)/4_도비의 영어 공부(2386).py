# 맞았습니다!

import sys

while(True):
    value = sys.stdin.readline().strip()
    if value == '#': # 입력값이 #일경우 나가기 
        exit(0)

    alphabet, sentence, count = value[0].lower(), value[1:].lower(), 0 # 단어, 문장, 카운트 수
 
    for i in sentence: # 해당 단어가 있으면 카운트
        if alphabet == i:
            count += 1
    
    print(alphabet, count) # 출력
        