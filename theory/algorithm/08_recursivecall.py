# 회문 프로그래밍 연습 

'''
문제
    1. 정수 n에 대해 
    2. n이 홀수이면 3*n+1을 하고,
    3. n이 짝수이면 n을 2로 나눕니다.
    4. 이렇게 계속 진행해서 n이 결국 1이 될 때까지 2와 3의 과정을 반복합니다.
'''
'''
# 내가 짠거
def calculate(num):
    if num == 1 :
        return num
    if num % 2 == 1:
        num = 3*num+1
        #print(num)
        return calculate(num)
    elif num %2 == 0:
        num = num/2
        #print(num)
        return calculate(num)
    

print(calculate(3))


def calculate(n):
    print(n)
    if n == 1 :
        return n
    if n % 2 == 1:
        return calculate((3*n)+1)
    else:
        return calculate(int(n/2))

print(calculate(3))
'''

'''
    문제
    정수 4를 1,2,3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
    1+1+1+1
    1+1+2
    1+2+1
    2+1+1
    2+2
    1+3
    3+1
    정수 n이 입력으로 주어졌을 때, n을 1,2,3의 합으로 나타낼 수 있는 방법의 수를 구하시오

    힌트 : 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 f(n)이라고 하면,
    f(n)은 f(n-1)+f(n-2)+f(n-3)이 동일하다는 패턴 찾기
'''

# 못품

def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    return func(data-1) + func(data-2) + func(data-3)

print(func(4))