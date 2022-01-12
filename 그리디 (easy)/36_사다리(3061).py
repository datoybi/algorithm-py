'''
맞았습니다!
문제는 이해했는데 어떻게 접근해야할 지 모르겠음 ㅠ
입력 데이터 수 T
사다리의 세로줄 N

bubble sort와 같다 i와 i-1중에 i-1 > i 면 inversion이 일어나서 
결국엔 1이 맨 앞으로 오고 정렬하면 된다.
'''

import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    ladder = list(map(int, sys.stdin.readline().split()))
    cnt, i, flag = 0, N-1, False

    while True:
        if i == 0:
            if flag == False:
                break
            i = N-1
            flag = False
        if ladder[i-1] > ladder[i]:
            ladder[i-1], ladder[i] = ladder[i], ladder[i-1]
            cnt += 1
            flag = True
            i -= 1
        else:
            i -= 1
    print(cnt)






