

'''
    탐욕 알고리즘의 예 
        문제1. 동전 문제 
            지불해야 하는 값이 4720원 일때 1원 50원 100원, 500원 동전으로 동전의 수가 가장 적게 지불하시오.
            가장 큰 동전부터 최대한 지불해야 하는 값을 채우는 방식으로 구현 가능
            탐욕 알고리즘으로 매순간 최적이라고 생각되는 경우를 선택하면 됨
            
    참고
        coin_list.sort(reverse=True) -> 내림차순으로 정렬
        data_list = sorted(data_list, key=lambda x:x[1]/x[0], reverse=True)

'''

coin_list = [100, 500, 50, 1]
# print(coin_list)
coin_list.sort(reverse=True)
# print(coin_list)

def calculate(coin_list, money):
    total = 0
    result = list()
    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_num = money // coin
        total += coin_num
        money -= coin_num * coin

        result.append([coin, coin_num])

    return total, result

            

print(calculate(coin_list,4561))


