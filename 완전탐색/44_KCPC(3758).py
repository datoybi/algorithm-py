'''

https://www.acmicpc.net/problem/3758

!점수 같고 제출 횟수 낮을수록 순위 높음 
!점수 같고 제출 횟수도 같은경우, 제출 시간이 빠른 경우

T(tc)
팀의 개수 n, 문제의 개수 k, 당신 팀의 id t, 로그 앤트리의 개수 m
    3 ≤ n, k ≤ 100, 1 ≤ t ≤ n, 3 ≤ m ≤ 10,000
m개의 줄
팀 id i, 문제번호 j, 획득한 점수 s
    1 ≤ i ≤ n, 1 ≤ j ≤ k, 0 ≤ s ≤ 100

'''
tc = int(input())

for _ in range(tc):
    score_lst, result_lst = list(), list()
    n, k, t, m = map(int, input().split()) 
    for log in range(m):
        score_lst.append(list(map(int, input().split())))
    
    for i in range(1, n+1):# 1 2 3
        total_score = 0
        tmp_lst = list()

        for j in range(m): # 로그만큼
            if score_lst[j][0] == i:
                print(i, score_lst[j])
                tmp_lst.append([score_lst[j][1], score_lst[j][2]])
                print('tmp_lst : ' , tmp_lst)

        for z in range(len(tmp_lst)-1): 
            if tmp_lst[z][1] == tmp_lst[z+1][1]: # 같은 문제 맞춘거 판별

                # 일단... 같은거 판별해서 토탈 입력하기. 제출 시간, 제출 횟수는 나중에 판별하기

                # print('같 ', tmp_lst[z][1], tmp_lst[z+1][1])
                # max_val = 
                # if tmp_lst[z][1] > tmp_lst[z+1][1]:
                #     tmp_lst.append([tmp_lst[z][0], tmp_lst[z][1]])
                #     d
                # else:
                #     del tmp_lst[z][]

            print('tmp_lst1 : ' , tmp_lst)




print(score_lst)
