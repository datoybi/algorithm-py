'''
    스택 Stack
        데이터를 제한적으로 접근할 수 있는 구조
        한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조
        가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조 
        큐:FIFO, 스택: LIFO(Last In First Out), FILO(First In, Last Out)

    대표적인 스택의 활용 
        컴퓨터 내부의 프로세스 구조의 함수 동작 방식

    주요 용어
        push() : 데이터를 스텍에 넣기 
        pop() : 데이터를 스텍에서 꺼내기
    
    장점
        구조 단순 구현 용이 
        데이터 저장/읽기 속도가 빠르다
    단점 
        데이터 최대 갯수를 미리 정해야 한다 ( 파이썬의 경우 1000번 까지만 호출 가능함)
        저장공간의 낭비가 발생 할 수 있음



# 재귀 함수
def recursive(data):
    if data < 0:
        print("ended")
    else :
        print(data)
        recursive(data-1)
        print("returned", data)
        
recursive(4)


실행결과
4
3
2
1
0
ended
returned 0
returned 1
returned 2
returned 3
returned 4

data_stack = list()
data_stack.append(1)
data_stack.append(2)
print(data_stack[0]) # 1

print(data_stack.pop()) # 2

'''

stack_list = list()
def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]  # 맨 끝에 있는 노드 가져오기!
    return data

for index in range(10): # 0~9
    push(index)
    print(index)
    
print(pop())
print(pop())