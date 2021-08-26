'''
    굉장히 중요 !

    제목 : 나이순 정렬
    난이도 : 하
    유형 : 정렬
    시간 : 15분
    
'''

# 맞는것 같은데 왜 틀렸다고 나오는지 모르겠음
num = int(input())
b_list = []

for _ in range(num):
    age, name = input().split(' ')
    b_list.append([age, name])
    
# print(b_list[0][0])

for i in range(len(b_list)-1):
    if b_list[i][0] > b_list[i+1][0]:
        b_list.insert(0, [b_list[i+1][0], b_list[i+1][1]])        
        del b_list[-1]

for j in b_list:
    print(j[0] , j[1])

#####################################################################
'''
    문제 풀이 핵심 아이디어 
    1. (나이,이름)의 정보를 입력 받은 뒤에 나이를 기준으로 정렬합니다.
    2. 파이썬의 기본 정렬 라이브러리를 이용하면 됩니다.
    3. 나이가 동일한 경우, 먼저 입력된 이름 순서를 따르도록 key 속성을 설정해야 합니다.
'''
# 해답

n = int(input())
array = []

for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]), input_data[1]))

array = sorted(array, key=lambda x: x[0]) #? 키가 무슨 소용
# array = sorted(array)
for i in array:
    print(i[0], i[1])

# 두번쨰시도 - 실패 