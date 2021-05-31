'''
    충돌(Collision) 해결 알고리즘
        해쉬 테이블의 가장 큰 문제는 충돌(Collision)의 경우다. 이 문제를 충돌(Collision) 혹은 해쉬 충돌(Hash Collision) 이라고 부릅니다.

   Chaining 기법
    개방 해싱 또는 open hashing 기법 중 하나. 해쉬 테이블 저장공간 외의 공간을 활용하는 기법 
    충돌이 일어나면, 링크드 리스트라는 자료구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법 

'''

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key%8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
            hash_table[hash_address].append([index_key.value])
        else:
            hash_table[hash_address] = [[index_key.value]]

    hash_table[hash_address] = value

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

print(hash('Dave') % 8)
print(hash('Dd') % 8)
print(hash('Data') % 8)


save_data('Dd', '1201023010')
save_data('Data', '3301023010')
read_data('Dd')
print(hash_table)