'''
맞았습니다! 
어우 까다롭다.. 겨우겨우 맞췄다.
처음엔 너무 쉽게 생각했다. 문제에서 제시한 순서를 따라가다보면 그래도 맞출 수 있는 문제.

반례
3
10
3 4 3 3 1 2 4 1 5 7

3 5 7

사진틀 N
전체 학생의 총 추천 횟수 (1000이하)
추천받은 학생을 나타내는 번호 (1~100까지 자연수)
'''

import sys

N = int(sys.stdin.readline()) 
int(sys.stdin.readline()) 
student = list(map(int, sys.stdin.readline().split()))
lst = list()

for i in range(len(student)): # 갯수 삽입
    # print(lst)
    # print(student[i])
    if len(lst) == 0: # 사진틀에 아무것도 없을 때 
        lst.append([student[i], 1, i])
    elif len(lst) < N: # 사진틀에 자리가 있을 때 
        flag = False
        for j in range(len(lst)): # 넣어주기
            if student[i] == lst[j][0]:
                lst[j][1] += 1
                flag = True
        if flag == False: # 안넣어졌다면 새로 만들기
            lst.append([student[i], 1, i])

    elif len(lst) == N: # 꽉 찼으면 -> 횟수가 가장 적은 학생의 사진 삭제, 횟수가 같으면 -> 게시된지 오래된거 삭제
            min_val, min_count, min_idx = lst[0][1], 0, 0
            flag = False
            tmp = list()
            for j in range(len(lst)): # 사진틀에 이미 있는 사람이라면 ++1 해주기 
                if student[i] == lst[j][0]:
                    lst[j][1] += 1
                    flag = True
                    break
            if flag == False: # 사진틀에 사람이 없다면 
                for j in range(len(lst)): # 가장 작은 횟수 추출
                    min_val = min(min_val,lst[j][1])
                for j in range(len(lst)): # 가장 작은 횟수가 몇개인지 카운트
                    if lst[j][1] == min_val:
                        tmp.append(lst[j]) # 가장 작은 것들 리스트에 담기
                        min_count += 1
                        min_idx = j
                if min_count == 1:
                    lst[min_idx] = [student[i], 1, i]
                else:
                    tmp = sorted(tmp, key=lambda x:x[2]) # 순서가 빠른거 앞으로 정렬
                    lst.remove(tmp[0])
                    lst.append([student[i], 1, i])

# 출력
lst = sorted(lst)
for i in lst:
    print(i[0], end=' ')




#####

# import sys

# N = int(sys.stdin.readline()) 
# int(sys.stdin.readline()) 
# student = list(map(int, sys.stdin.readline().split()))
# lst = list()
# print(student)
# result = list()
# count = 0

# for i in range(len(student)): # 갯수 삽입
#     lst.append((student[i], student.count(student[i]), i))
# print(lst)

# arranged = sorted(lst, key=lambda x:(-x[1], -x[2]))
# print('arranged : ' , arranged)

# for i in range(len(arranged)):
#     if count <= N-1 and arranged[i][0] not in result :
#         result.append(arranged[i][0])
#         count += 1

# result = sorted(result)

# for i in result:
#     print(i, end=' ')