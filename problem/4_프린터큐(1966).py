"""
    제목 : 프린터 큐
    난이도 : 하
    유형 : 큐, 구현, 그리디
    시간 : 25분
    느낀점 : 문제 이해를 못하겠음 ㅠㅠ 해답 봐도 이해 불가넝.. 다음에 해보기

    문제 풀이 핵심 아이디어
        1. 데이터의 개수(N <= 100)가 많지 않으므로, 단순히 문제에서 요구하는 대로 구현합니다.
        2. 현재 리스트에서 가장 큰 수가 앞에 올 때까지 회전시킨 뒤에 추출합니다.
        3. 가장 큰 수가 M이면서 가장 앞에 있을 때 프로그램을 종료합니다. 

    느낀점 : 아오 두번째봐도 이해가 안된다 씨뻘..
"""

test_case = int(input())

for _ in range(test_case):
    n,m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    print(queue) # [(5, 0)] , [(1, 0), (2, 1), (3, 2), (4, 3)] , [(1, 0), (1, 1), (9, 2), (1, 3), (1, 4), (1, 5)]
    
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]: # 키값을 가져오는
            count += 1
            if queue[0][1] == m: # value가 맞으면
                print(count) 
                break
            else:
                queue.pop(0) # 안맞으면 뽑았다가 뒤에다 붙이기
        else:
            queue.append(queue.pop(0)) # 뒤에 붙이기


