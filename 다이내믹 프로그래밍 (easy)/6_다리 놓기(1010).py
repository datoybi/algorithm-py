'''
나중에 풀어보기 conbination인 조합을 사용해야 하는지 첨 알았당
다만 dp를 사용하지 않았다.. 이건 다음에 고민해보아야겠다.

m! // (n! * m-n!)
n! / ((n - m)! * m!) 

n = 29, m = 13
n! / ((n - m)! * m!) = 67863915
'''

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)


# def factorial(n):
#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num


# T = int(input())

# for _ in range(T):
#     n, m = map(int, input().split())
#     bridge = factorial(m) // (factorial(n) * factorial(m - n))
#     print(bridge)