"""
    제목 : 피보나치 수 
    난이도 : 하
    유형 : 재귀함수
    시간 : 15분
"""

# 얼탱없게 시간초과 뜸 ㅠ 
# 내 코드가 실패 소스코드 예제로 뜸 
# def fibo(num):
#     if num <= 1:
#         return num
#     return_value = fibo(num-1) + fibo(num-2)
#     return return_value


# num = int(input())
# print(fibo(num))

# 해답
n = int(input())
a, b = 0, 1

while n > 0:
    a, b = b, a+b
    n -= 1

print(a)

# 두번째 시도 이렇게 해서 안됐다 또 시간초과.. 
# 시간초과 안되는 걸로 해봤는데 이해 될랑말랑함ㅠ

n = int(input())

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))
