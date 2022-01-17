'''
맞았습니다!

최고의 피자 : 1원당 열량이 가장 높은 피자
같은 종류의 토핑을 2개 이상 선택할 수는 없다. 또, 토핑을 전혀 선택하지 않을 수도 있다.
피자 가격 = 도우의 가격 + 토핑의 가격 * 토핑의 종류

3
1 10
300
100
50
200

답:300
'''

import sys

N = int(sys.stdin.readline())
dough_price, topping_price = list(map(int, sys.stdin.readline().split()))
dough = int(sys.stdin.readline())
toppings = list()
for i in range(N):
    toppings.append(int(sys.stdin.readline()))
toppings.sort(reverse=True)
result = 0

for i in range(len(toppings)+1):
    total_price = dough_price + topping_price * (i)
    total_cal = sum(toppings[:i]) + dough
    print((total_cal // total_price))
    result = max(result, (total_cal // total_price))

print(result)