'''
    맞았습니다!
    1 <= N <= 1000
    
'''
import sys

# 데이터 입력
N = int(sys.stdin.readline())
lst, result = list(), 0

for i in range(N):
    lst.append(int(sys.stdin.readline()))

for i in range(len(lst)):
    delete_num, tmp_lst = lst[i], list() # 지울 숫자, 특정 숫자가 지워진 임시 리스트

    for j in range(len(lst)): # 삭제한 리스트 만들기
        if delete_num != lst[j]: 
            tmp_lst.append(lst[j])
            
    # print(tmp_lst)
    max_val, tmp_val = 1, 1 # 카운트 값
    for z in range(len(tmp_lst)-1):
        if tmp_lst[z] == tmp_lst[z+1]:
            tmp_val += 1 
        else:
            max_val = max(max_val, tmp_val)
            tmp_val = 1
            #만약에 다음 수가 같은 수가 아니면, tmp_val이 max_val에 저장되고, tmp_val이 초기화 되어야 한다  
        max_val = max(max_val, tmp_val)
    if result < max_val:
        result = max_val
            
print(result)



# 남의 코드 - 간결해서 가져와봤다.

import sys

# 입력 받을 개수
n = int(sys.stdin.readline())

# 값 입력받기
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

# 결과 변수 및 이미 한 번 체크하였었던 수인지를 확인하기 위한 리스트 선언
result = 0
already = [0] * 1000001 # 0으로 다 채운 list

# print(already)

# 확인 진행
for i in data:
    # print(already[i]) # 0 이나 1
    if already[i]: 
        continue
    already[i] = 1 # 반복하지 않기위해 사용
    cur = data[0] # 2
    cnt = 1
    for j in range(1 ,len(data)):
        if i == data[j]: # i(삭제할 숫자)랑 data[j] 같으면 continue
            continue
        if cur == data[j]: # cur이랑 같으면 +1
            cnt += 1
        else: # 다르면 cnt = 1
            cur = data[j]
            cnt = 1
        result = max(result, cnt)

print(result)