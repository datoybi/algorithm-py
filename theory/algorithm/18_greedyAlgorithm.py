'''
탐욕 알고리즘(Greedy Algorithm)
    최적의 해에 가까운 값을 구하기 위해 사용됨
    여러 경우 중 하나를 결정해야할 때마가, 매순간 최적이라고 생각되는 경우를 선택하는 방식으로 진행해서, 최종적인 값을 구하는 방식
'''

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

coin_list = [500,100,50,1]

def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin 
        details.append([coin, coin_num])

    return total_coin_count, details

#print(min_coin_count(4720, coin_list))

'''
    문제2. 부분 배낭 문제(Fractional Knapsack Problem)
    무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
        각 물건은 무게(w)와 가치(v)로 표현될 수 있음 
        물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음, 그래서 Fractional Knapsack Problem으로 부름
            Fractional Knapsack Problem의 반대로 물건을 쪼개서 넣을 수 없는 배낭 문제도 존재함 (0/1 Knapsack Problem으로 부름)

                    물건1   물건2   물건3   물건4   물건5
            무게    10      15      20      25      30
            가치    10      12      10      8       10

'''
        
data_list = [(10,10),(15,12),(20,10),(25,8),(30,5)]

def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x:x[1]/x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0] # 0보다 크다는 것은 capacity보다 더 작다는 거니까 통째로 넣으면 됨
            total_value += data[1] # total_value에 가치 통째로 넣기
            details.append([data[0],data[1],1]) # [무게, 가치, 1(몇프로 넣었는지)]
        else:
            fraction = capacity / data[0] # 요부분이 좀 헷갈림
            # capacity -= data[0] * fraction 당연히 capacity가 0이 되니까 지움
            total_value += data[1] * fraction
            details.append([data[0],data[1],fraction])
            break
    return total_value, details


print(get_max_value(data_list, 30))


'''
탐욕 알고리즘의 한계 
    탐욕 알고리즘은 근사치 추정에 활용
    반드시 최적의 해를 구할 수 있는 것은 아니기 때문
    최적의 해에 가까운 값을 구하는 방법 중의 하나임 
    예 : 시작 노드에서 시작해서 가장 작은 값을 찾아 leaf node까지 가는 경로를 찾는 경우

'''