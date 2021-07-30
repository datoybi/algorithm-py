"""
    제목 : 스택 수열 
    난이도 : 하
    유형 : 스택, 그리디
    시간 : 30분
    느낀점 : 문제를 이해 못하겠음ㅜ, 문제 해석 잠깐 보고 이해함
            변수 많이 만들 필요도 없고 뒤에서 무슨 일 일어나는지도 안 중요함 -> '중요한건 주어진 절차에 의거하여 결과값이 잘 나오는지' 이다
"""

# count = int(input())
# inputArr = []
# makingList = []
# stack = []

# for i in range(0, count):
#     inputArr.append(int(input()))

# # print("\n")
# # print(inputArr[0])
# # del inputArr[0]
# # print(inputArr[0])

# for j in range(1, 100): # 1~100까지 스텍 만들기
#     print(inputArr[0]) # 4
#     stack.append(j) # 1 2 3 4

#     if inputArr[0] != stack[j]:
#         # print(inputArr[k])
#         print('+')

#     elif inputArr[0] == j:
#         print('-')
#         del stack[j]
#         del inputArr[0]
    
# # print(inputArr)


# n = int(input())
# count = 1
# result = []
# stack = []

# for i in range(1, n+1): # 데이터 개수만큼 반복
#     data = int(input())
#     while count <= data: # 입력 받은 데이터에 도달할 때까지 삽입
#         stack.append(count)
#         count += 1
#         result.append('+')
#     if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때 출력
#         stack.pop()
#         result.append('-')
#     else: # 불가능한 경우
#         print('NO')
#         exit(0)

# print('\n'.join(result)) # 가능한 경우

n = int(input())
result = []
stack = []
count = 1

for i in range (1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else :
        print('NO')
        exit(0)

print('\n'.join(result))
