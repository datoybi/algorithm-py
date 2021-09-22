"""
    제목 : 키로거
    난이도 : 중
    유형 : 스택, 구현, 그리디
    시간 : 40분
    느낀점 : 어떻게 풀어야 되는지 감도 안잡힘;
    문제 풀이 핵심 아이디어 : 
    1. 문자열 크기가 최대 1,000,000이므로 시뮬레이션 방식으로는 문제를 해결할 수 없습니다.
    2. 스택을 활용하여 선형시간 문제를 해결할 수 있는 알고리즘을 설계합니다.
        1) 스택 두 개를 만들고, 스택 두개의 중간 지점을 커서(cursor)로 간주합니다.
        2) 문자 입력 : 왼쪽 스택에 원소를 삽입합니다.
        3) - 입력 : 왼쪽 스택에서 원소를 삭제합니다.
        4) < 입력 : 왼쪽 스택에서 오른쪽 스택으로 원소를 이동합니다.
        5) > 입력 : 오른쪽 스택에서 왼쪽 스택으로 원소를 이동합니다.

"""

# test_case = int(input())

# for _ in range(test_case):
#     left_stack = []
#     right_stack = []
#     data = input()

#     for i in data:
#         if i == '-':
#             if left_stack:
#                 left_stack.pop()
#         elif i == '<':
#             if left_stack:
#                 right_stack.append(left_stack.pop())
#         elif i == '>':
#             if right_stack:
#                 left_stack.append(right_stack.pop())
#         else:
#             left_stack.append(i)
#     left_stack.extend(reversed(right_stack))
#     print(''.join(left_stack))
    
test_case = int(input())

for _ in range(test_case):
    right_stack = []
    left_stack = []
    data = input()

    for i in data:
        if i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif i == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))


        













