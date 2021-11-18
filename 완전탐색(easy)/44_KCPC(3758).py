'''
맞았습니다! 다음에 꼭 풀어보기 

하 .. 이거 풀어보려 햇는데 어캐 구현해야 할지 막막함 특히.. 내가 구현한 방법은 제출시간이 빠른 경우는 판별할 수 없다. 
딕셔너리를 사용해야하는지 리스트를 사용해야 하는지. .튜플은 아닌것 같고(변경이 안되니까)
잘 모르겠다.. .ㅠ  

-> 리스트를 사용하는게 맞고, 필요한 것들 입력받을때 가공한 뒤, 나중에 정렬한 후 나의 팀 추출하기



!점수 같고 제출 횟수 낮을수록 순위 높음 
!점수 같고 제출 횟수도 같은경우, 제출 시간이 빠른 경우

T(tc)
팀의 개수 n, 문제의 개수 k, 당신 팀의 id t, 로그 앤트리의 개수 m
    3 ≤ n, k ≤ 100, 1 ≤ t ≤ n, 3 ≤ m ≤ 10,000
m개의 줄
팀 id i, 문제번호 j, 획득한 점수 s
    1 ≤ i ≤ n, 1 ≤ j ≤ k, 0 ≤ s ≤ 100

1
3 4 3 5
1 1 30
2 3 30
1 2 40
1 2 20
3 1 70

'''

# 남의 코드
import sys

T = int(sys.stdin.readline())
# [id, score1, score2, score3, score4, 최종점수, 제출횟수, 제출시간]

for _ in range(T): # Test Case
    n, k, t, m = map(int, sys.stdin.readline().split())
    arr = [[0]*(k+4) for _ in range(n)] # 아이디개수 만큼 배열 생성 , k+4인 이유는 k가 문제 갯수니까  [id, score1, score2, score3, score4, 최종점수, 제출횟수, 제출시간]로 만들거기 때문에.

    # id setting
    for i in range(n):
        arr[i][0] = i+1
    # print(arr) 
    # [[1, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0]]

    # score, time setting
    for time in range(m):
        i, j, s = map(int, sys.stdin.readline().split()) # id(0~3), 문제번호(0~3), 점수
        arr[i-1][j] = max(arr[i-1][j], s) # 이미 맞춘 or 방금 푼 문제 중 큰 거
        arr[i-1][k+2] += 1 # 제출 횟수 
        arr[i-1][k+3] = time # 마지막 제출 시간

    # print(arr)
    # [[1, 30, 40, 0, 0, 0, 3, 3], [2, 0, 0, 30, 0, 0, 1, 1], [3, 70, 0, 0, 0, 0, 1, 4]]

    # total score setting
    for i in range(n):
        for j in range(1, k+1):
            arr[i][k+1] += arr[i][j]
    
    # 정렬
    ans = sorted(arr, key = lambda x: (-x[k+1], x[k+2], x[k+3])) # 우선순위 별로 정렬
    # print(ans)
    
    # 내 팀 찾기
    for i in range(n):
        if ans[i][0] == t:
            print(i+1)
            break



# 풀다만 내코드 ㅠ 담에 꼭 다시 풀어보쟈

# tc = int(input())

# for _ in range(tc):
#     score_lst, result_lst = list(), list()
#     n, k, t, m = map(int, input().split()) 
#     for log in range(m):
#         score_lst.append(list(map(int, input().split())))

#     max_val = 0

#     for i in range(1, n+1):# 1 2 3
#         log_count = 0
#         tmp_lst = list()

#         for j in range(m): # 로그만큼
#             if score_lst[j][0] == i:
#                 log_count += 1
#                 print(i, score_lst[j])
#                 tmp_lst.append([score_lst[j][1], score_lst[j][2]])
#                 print('tmp_lst : ' , tmp_lst)

#         for z in range(len(tmp_lst)-1): 
#             if tmp_lst[z][0] == tmp_lst[z+1][0]: # 같은 문제 맞춘거 판별
#                 if tmp_lst[z][1] > tmp_lst[z+1][1]:
#                     del tmp_lst[z+1]
#                 else:
#                     del tmp_lst[z]

#         tmp_sum = 0 
#         for t in tmp_lst: # 총 점수 구하기
#             tmp_sum += t[1]
#             # print('t ' , sum(t[1]))
#         # print('!!!tmp_sum : ' , tmp_sum)
#         result_lst.append([i, tmp_sum, log_count])


#     print(max_val)
#     # max_val = 0
#     winner = ''
#     max_lst = []

#     for item in range(n):
#         if max_val < result_lst[item][1]:
#             max_val = result_lst[item][1]
    
#     for item in range(n):
#         if max_val == result_lst[item][1]:
#             max_lst.append()
            


# print(result_lst)
