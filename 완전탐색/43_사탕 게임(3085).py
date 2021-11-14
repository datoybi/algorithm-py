'''
맞았습니다! 뭔가 깔끔하게 해결된 기분? 완벽히 문제를 이해한 기분이다....
문제를 봐도 이해가 안되냐 왜 
아! 이해함
딱 하나의 사탕의 위치를 변경하여 최대의 사탕(연속된 색깔의 사탕들)을 먹어야 한다. 

3 <= N <= 50

놓친부분 : 인.접. 하다고 했으니까 세로도 바꿔야됨
반례들.. 
2
CC
YY
0
'''
import copy

candy_lst, max_val = list(), 0
# 입력
for _ in range(int(input())):
    candy_lst.append(list(input())) 

for i in range(len(candy_lst)):
    for j in range(len(candy_lst[i])-1):
        h_tmp_lst, v_tmp_lst = copy.deepcopy(candy_lst), copy.deepcopy(candy_lst) # 기존의 캔디 리스트를 딥카피
        
        # 사탕 위치 바꾸기 (h_tmp_lst: 가로 바꾸기, v_tmp_lst: 세로 바꾸기)
        h_tmp_lst[i][j], h_tmp_lst[i][j+1] = h_tmp_lst[i][j+1], h_tmp_lst[i][j] # if 조건을 걸면 안됨 (아예 for문이 안돌수도 있기 때문) 
        v_tmp_lst[j][i], v_tmp_lst[j+1][i] = v_tmp_lst[j+1][i], v_tmp_lst[j][i]
        
        # print(tmp_lst, tmp_lst1)
        # 사탕 최대값 판별
        for a in range(len(candy_lst)):
            tmp_max, v_val, v_val1, h_val1, h_val = 0, 1, 1, 1, 1
            for b in range(len(candy_lst[i])-1):        
                # 가로         
                if h_tmp_lst[a][b] == h_tmp_lst[a][b+1]: # 같으면 1 추가
                    h_val += 1
                else: # 같지 않으면 값 초기화
                    h_val = 1
                if h_tmp_lst[b][a] == h_tmp_lst[b+1][a]:
                    v_val += 1
                else:
                    v_val = 1

                #세로
                if v_tmp_lst[a][b] == v_tmp_lst[a][b+1]:
                    h_val1 += 1
                else:
                    h_val1 = 1
                if v_tmp_lst[b][a] == v_tmp_lst[b+1][a]:
                    v_val1 += 1
                else:
                    v_val1 = 1

                if tmp_max < max(v_val, h_val, v_val1, h_val1):
                    tmp_max = max(v_val, h_val, v_val1, h_val1)
                # print(v_val, h_val, v_val1, h_val1, tmp_max)

            if max_val < tmp_max:
                max_val = tmp_max

print(max_val)

