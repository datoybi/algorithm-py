'''
    맞았습니다!!
    
    문제 잘 보기 -> 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수!!!!!!!!!!!!!!


    스트라이크 : 동일한 자리, 동일한 수
    볼 : 다른 자리, 동일한 수

    N : 자연수 N, 몇번이나 질문을 했는지 (1 <= N <= 100)
    세자리수, 스트라이크, 볼
    4
    123 1 1
    356 1 0
    327 2 0
    489 0 1

    2 324와 328,

    3
    567 0 0
    812 0 2
    193 2 0
    답 : 3

    3
    123 1 0
    269 0 2
    461 0 1
    답 : 8

'''

n_lst, s_lst, whole_lst = list(), list(), list()
N = int(input())

for _ in range(0, N): # 값 넣기
    lst = list(map(int, input().split()))
    n_lst.append(lst[0])
    s_lst.append([lst[1], lst[2]])

for i in range(101,999): # 101~998
    count = 0
    tmp = list(str(i))
    if tmp[0] == tmp[1] or tmp[0] == tmp[2] or tmp[1] == tmp[2] or '0' in tmp : # 중복되지 않고 0이 아닌 세자릿 수
        continue
    # print(tmp)

    for j in range(len(n_lst)):
        num = list(str(n_lst[j]))
        # print(num, tmp)
        strike, ball = 0, 0
        # print('num : ' , num)
        for z in range(3):
            if num[z] == tmp[z]: # 스트라이크인지 ?
                strike += 1
            elif num[z] in tmp : # 볼인지 ?
                ball += 1
        # print(i, n_lst[j], strike, ball)
        if strike == s_lst[j][0] and ball == s_lst[j][1]:
            count+=1
            # print(strike, ball,  s_lst[j][0], s_lst[j][1] )
    if count == N:
        whole_lst.append(i) 
        
# print(whole_lst)
print(len(whole_lst))

