'''
    제목 : 0 만들기
    난이도 : 중
    유형 : 재귀함수
    시간 : 40분
    ???????????

    문제풀이 핵심 아이디어 
        1. 가능한 모든 경우를 고려하여 연산자 리스트를 만드는 것이 관건입니다. (재귀함수 이용)
        2. 파이썬의 eval()함수를 이용하여 문자열 형태의 표현식을 계산할 수 있습니다.
'''
import copy

def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

test_case = int(input())

for _ in range(test_case):
    operators_list = []
    n = int(input())
    recursive([], n-1)

    integers = [i for i in range(1, n+1)]
    
    for operators in operators_list:
        string = ""
        for i in range(n-1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()

#두번쨰 시도 : 못품 