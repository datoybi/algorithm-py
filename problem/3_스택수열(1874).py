"""
    제목 : 스택 수열 
    난이도 : 하
    유형 : 스택, 그리디
    시간 : 30분
    느낀점 : 문제를 이해 못하겠음ㅜ, 문제 해석 잠깐 보고 이해함
"""



count = int(input())
inputArr = []
makingList = []
stack = []

for i in range(0, count):
    inputArr.append(int(input()))

for k in range(0, count):
    for j in range(1, 100):
        print(inputArr[k])
        stack.append(j)

        if inputArr[k] != stack[j]:
            # print(inputArr[k])
            print('+')
            break;

        elif inputArr[k] == j:
            print('-')
            del stack[j]
            continue;
    
# print(inputArr)
