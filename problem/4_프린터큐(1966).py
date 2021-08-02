"""
    제목 : 프린터 큐
    난이도 : 하
    유형 : 큐, 구현, 그리디
    시간 : 25분
    느낀점 : 문제 이해를 못하겠음 ㅠㅠ 해답 봐도 이해 불가넝.. 다음에 해보기
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


