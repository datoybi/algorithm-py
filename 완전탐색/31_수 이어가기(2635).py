'''
맞았습니다!

100, 60, 40, 20, 20 , 0, 20
100, 62, 38, 24, 14, 10, 4, 6

100
8
100 62 38 24 14 10 4 6
첫번째 수 
최대개수
수출력
'''

N = int(input())
answer_lst = list()
count = 0

if N < 0: # 입력값이 음수일 때 처리
    exit(0)

for i in range(N-1, -1, -1): # 99~0
    tmp_lst = [N]
    tmp_lst.append(tmp_lst[-1] - i)

    while(True): # 뺀 수가 음수이면 나가기
        # print(tmp_lst[-2] , tmp_lst[-1], tmp_lst[-2] - tmp_lst[-1])
        if tmp_lst[-2] - tmp_lst[-1] >= 0:
            tmp_lst.append(tmp_lst[-2] - tmp_lst[-1])
            # print(tmp_lst)
        else: 
            break
    if count < len(tmp_lst):
        count = len(tmp_lst)
        answer_lst = tmp_lst

print(count)
for i in answer_lst:
    print(i, end=' ')
