'''
    굉장히 중요 !

    제목 : 나이순 정렬
    난이도 : 하
    유형 : 정렬
    시간 : 15분
    
'''

num = int(input())
b_list = []

for _ in range(num):
    age, name = input().split(' ')
    b_list.append([age, name])
    
print(b_list[0][0])

for i in range(len(b_list)):
    
