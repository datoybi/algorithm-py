'''
맞았습니다!
이거 외국문제라 이해하는데 좀 시간이 걸렸다.
핵심은.. 나머지 아이들이 가지고 있는 음식의 총 합보다 해당 아이가 가진 합이 더 크면 혼내야한다.

그리고 잡으려고 하는 쿠키는 위의 것을 판별할 때 포함하지 않는다.

#####
제가 이 문제 이해한바로는 한 줄 마다 아이 이름을 하나씩 읽고, 
얘가 현재 갖고 있는 쿠키의 갯수와 
나머지 다른 아이들이 가져간 갯수의 합을 비교해서 
앞에 것이 더 크면 혼내고 아니면 하나씩 올리는 대로 정확히 
코딩했는데 자꾸 틀렸다고 하네요

만약, 어떤 어린이가 쿠키를 집는 그 순간에, 
다른 아이들이 가지고 있는 쿠키 개수의 합 보다 많은 쿠키를 가지고 있다면, 
선생님에게 혼나게 된다. (집으려고 하는 쿠키는 포함하지 않는다)

가져가려고 하는 어린이가 다른 어린이들을 합한값보다 더 클때

1~100명까지 가능 key value 쌍으로 넣을 수 있어야 할듯.. -> 이중리스트 

'''

import sys

N = int(sys.stdin.readline())
lst = []
lst.append([sys.stdin.readline().rstrip(),1])
count = 0

for _ in range(N-1):
    now = sys.stdin.readline().rstrip()
    check, sum, now_idx = False, 0, 0

    for i in range(len(lst)): 
        if lst[i][0] == now: 
            check = True # 갯수 더하기를 위한 bool 값
            now_idx = i # 갯수 더하기를 위한 index 값
        else:
            sum += lst[i][1] # 나머지값 구하기 
    # print(sum, lst[now_idx][1], count)
    if sum < lst[now_idx][1]: # 나머지값들보다 작으면 혼내기
        count += 1

    if check == False:
        lst.append([now,1]) 
    else:
        lst[now_idx][1] += 1

print(count)