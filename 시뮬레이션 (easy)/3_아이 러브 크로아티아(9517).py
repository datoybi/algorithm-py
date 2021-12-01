'''
맞았습니다!

    T 이면 왼쪽 플레이어에게 넘겨줌
    N P이면 그 즉시 다음 문제 
  
    폭탄을 들고있는 사람의 번호 1 <= K <= 8
    질문의 개수 1 <= N <= 100
    i번째 질문을 대답하기까지 걸린 시간(1 <= T <= 100) 대답 Z(T, N, P)
 
    총 시간 210초
5
6
70 T
50 P
30 N
50 T
30 P
80 T

1
10
1 T
1 T
1 T
1 T
1 T
1 T
1 T
1 T
1 T
1000 T


'''

import sys

K, lst = int(sys.stdin.readline()), list()

for i in range(int(sys.stdin.readline())):
    T, Z = list(map(str, sys.stdin.readline().split()))
    lst.append([int(T), Z]) # [[70, 'T'], [50, 'P'], [30, 'N'], [50, 'T'], [30, 'P'], [80, 'T']]

i, time = 0, 0

while True:
    time += lst[i][0]
    
    if time >= 210:
        print(K)
        break

    if lst[i][1] == 'T': # T면 다음사람
        if K < 8:
            K += 1
        else:
            K = 1 

    if i == len(lst)-1: # i 길이 설정
        i = 0
    else:
        i += 1



    # if lst[i][1] == 'T':
    #     time += lst[i][0]
        
    # else:
    #     i += 1 
    #     time += lst[i][0]

    # print(i, K, time)

    # if time >= 210:
    #     print('answer : ' , K )
    #     break

    # if K < 8:
    #         K += 1
    # else:
    #     K = 0
    # i += 1



