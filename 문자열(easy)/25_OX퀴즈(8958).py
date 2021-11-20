# 맞았습니다!
import sys

for _ in range(int(sys.stdin.readline())):
    result, cnt, score = sys.stdin.readline().rstrip(), 1, 0

    for i in range(len(result)):
        if result[i] == 'O':
            score += cnt
            cnt += 1
        else:
            cnt = 1
        
    print(score)