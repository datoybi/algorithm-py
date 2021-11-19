# 맞았습니다!

import sys

for _ in range(3):
    count, value, answer = 1, 0, 1 # 같은단어가 있으면 카운트, 비교할 값, 정답
    num = sys.stdin.readline().strip() # 입력 

    for i in range(len(num)):
        if value == num[i]: # value와 같은 값이면 +1
            count += 1
        else:               # 다른 값이면 value를 현재값으로 넣기
            value = num[i]
            count = 1

        answer = max(answer, count)
        
    print(answer)