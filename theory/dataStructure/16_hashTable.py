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

def hash_function(key): # 나머지 8에 들어간다는 거니까 0~7까지 공간에 들어감 총 8
    return key%8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: 
        for index in range(len(hash_table[hash_address])): # 다른 key,value가 이미 들어있으면 
            if hash_table[hash_address][index][0] == index_key: # index번째의 키가 index_key와 같으면
                hash_table[hash_address][index][1] = value # 그 키값에 value 업데이트
                return
            hash_table[hash_address].append([index_key, value]) # 이미 삽입된 동일한 키가 없으면 새로 만들어서 붙이기
    else: # hash_table[hash_address] == 0
        hash_table[hash_address] = [[index_key, value]]

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


'''
[
	[
		[6782408722356686082, '1'], 
		[-8142135132873710882, '2'], 
		[-1483869573095058722, '4'], 
		[-1483869573095058722, '4']
	], 
	[
		[4212028575406034377, '3']
	]
]
'''