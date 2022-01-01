# 맞았습니다!
# 반례 abcc absdacadssdc

import sys

while True:
    try:
        s, t = list(map(str, sys.stdin.readline().split()))                
        result, idx = list(), 0
        for i in range(len(s)):
            for j in range(idx, len(t)):
                if s[i] == t[j]:
                    result.append(j)
                    idx = j+1
                    break
        print(result)
        # 출력     
        if len(result) != len(s): 
            print('No')
        else:
            if sorted(result) == result:
                print('Yes')
            else:
                print('No')
    except:
        break
