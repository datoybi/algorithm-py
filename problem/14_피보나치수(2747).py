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