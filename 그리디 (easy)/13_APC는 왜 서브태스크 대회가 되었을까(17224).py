'''
맞았습니다!
아 근데 실제로 풀수 있는지 없는지만 판별하면 되니까.. 
    쉬운버전(100), 어려운버전(40) 총 140
    쉬운버전만 맞추더라도 부분점수 
    쉬운 버전의 난이도 순으로 배치
    어려운 버전을 풀면 1문제로 계산 
    
    문제 개수 N, 역량 L, 풀수있는 최대 문제의 개수 K
    N개의 줄에 걸쳐 쉬운 버전의 난이도, 어려운 버전의 난이도

'''

import sys

# 입력
N, L, K = list(map(int, sys.stdin.readline().split()))
quiz = list()

for i in range(N):
    easy, hard = list(map(int, sys.stdin.readline().split()))
    quiz.append((easy, hard))

# 연산
cnt, score, flag = 0, 0, False
for i in range(N):
    flag = False
    if cnt == K: break 
    # quiz를 모두 돌면서 쉬운문제, 어려운 문제를 풀 수있는지 check
    for j in range(len(quiz)): 
        if quiz[j][0] <= L and quiz[j][1] <= L:
            cnt += 1
            score += 140
            flag = True
            del quiz[j]
            break
    # 둘다 풀수 없다면 쉬운문제만 풀 수 있는지 check
    if flag == False:
        for j in range(len(quiz)):
            if quiz[j][0] <= L:
                cnt += 1
                score += 100
                del quiz[j]
                break
print(score)

