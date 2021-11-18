'''
    맞았습니다!
    N명의 사람
    1~10사이의 수 다섯장
    세장을 골라 합을 구한 후 일의 자리 수가 가장 큰 사람이 이김 

'''
N = int(input())
card_lst = list()

for i in range(N):
    card_lst.append(list(map(int, input().split())))

result_lst = list() 
for item in range(len(card_lst)):
    score = 0
    for i in range(5):
        for j in range(i+1, 5):
            for z in range(j+1, 5):
                # print(card_lst[item][i], card_lst[item][j], card_lst[item][z])
                tmp_score = (card_lst[item][i] + card_lst[item][j] + card_lst[item][z]) % 10
                
                if score < tmp_score:
                    score = tmp_score

    result_lst.append([item+1, score]) 

max_val = max(t[1] for t in result_lst)

for i in range(len(result_lst)-1, -1 , -1):# 중복일 때 큰 수를 먼저 출력하기위해 거꾸로
    # print(result_lst[i][1], result_lst[i][0])
    if result_lst[i][1] == max_val:
        print(result_lst[i][0])
        exit(0)
    
