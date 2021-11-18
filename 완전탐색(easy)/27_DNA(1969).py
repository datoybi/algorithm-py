# 문제를 잘못 읽음 ㅠ 아오,,, 문제 알아먹기 왤케 힘드냐..
'''
    아오.... 죵나 문제 이해만 몇시간 째인지... 짜증난다 
    haming distance 찾는데서 좀 헤맸다. 솔직히 지금 봐도 이게 왜 그 의미인지 모르겠다
    문제가 이해되지 않을 때는 너무 붙잡고 있지말고 다른 글들을 참고하는 것도 좋은 것 같다
    그래도 결국은...
    맞았습니다!
'''

N,M = map(int, input().split())
lst = list()

for i in range(N): # 입력값 받기
    lst.append(input())

ans_lst = list()

for i in range(0, M): # 입력값을 세로로 원소를 두는 리스트 생성
    tmp_lst = list()
    for j in range(0, N):
        tmp_lst += list(lst[j][i])
    ans_lst.append(tmp_lst)

# print("ans_lst : " , ans_lst)

result_lst = list()

for i in range(len(ans_lst)): 
    max_value = ''
    max_count = 0
    for j in range(len(ans_lst[0])):
        tmp_cnt = ans_lst[i].count(ans_lst[i][j]) # 원소 하나씩 카운트해서 최소 Hamming Distance를 가진 DNA 찾기
        # print(ans_lst[i] ,ans_lst[i][j])        
        # print("tmp_cnt : " , tmp_cnt , " , i[j] : " , i[j])

        if max_count < tmp_cnt: 
            max_count = tmp_cnt
            max_value = ans_lst[i][j]
        elif max_count == tmp_cnt:
            if max_value > ans_lst[i][j]:
                max_value = ans_lst[i][j]

    result_lst.append(max_value)

 # Hamming Distance 찾기... 여기서 헤매었다. 
 # 나는 가로로 해서 답이 나오는 줄 알았는데 
 # 세로로 만든 리스트 즉 ans_lst로 답을 구해야하는거였다.. 
 # 이거때문에 얼마나 헤맸는지 모르겠다ㅠㅠㅠ

distance = 0
for i in range(len(ans_lst)): 
    for j in range(len(ans_lst[0])):
        if ans_lst[i][j] != result_lst[i]:
            distance+=1

#출력
result = ''
for i in result_lst:
    result += i

print(result)
print(distance)