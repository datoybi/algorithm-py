'''
    빈번한 충돌을 개선하는 기법
        해쉬 함수를 재정의 및 해쉬 테이블 저장공간을 확대 
        
    참고
        해쉬 함수와 키 생성 함수 
            파이썬의 hash() 함수는 실행할 때마다, 값이 달라질 수 있음
            유명한 해쉬 함수들이 있음 SHA(Secure Hash Algorithm) : 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해쉬함수로 유용하게 활용 가능

'''

import hashlib
'''
#SHA1 
data = 'test'.encode() #바이트로 바꿔준다
hash_object = hashlib.sha1()
hash_object.update(b'test') # data
hex_dig = hash_object.hexdigest()
print(hex_dig) # a94a8fe5ccb19ba61c4c0873d391e987982fbbd3

# 블록체인에서 이런 해쉬함수 사용
data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest() # 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
print(hex_dig) 
'''

#sha256으로 바꾸기
hash_table = list([0 for i in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16) # 16진수 정수로 형변환

def hash_function(key):
    return key%8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value # 만약에 이미 키가 동일하고 다른 벨류가 저장되어 있을 시, 벨류를 업데이트
                return
    else:
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None   
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

print(get_key('dv')%8)
print(get_key('dp')%8)
print(get_key('dc')%8)

save_data('dv','10923810923123')
save_data('dp','33333333333333')
print(read_data('dc'))

'''
    시간복잡도 
        일반적인 경우(충돌이 없는 경우) : O(1)
        최악의 경우(충돌이 모두 발생하는 경우) : O(n)
        해쉬테이블의 경우 일반적인 경우를 기대하고 만들기 때문에 O(1)이라고 말할 수 있음

        검색에서 해쉬 테이블의 사용 예 
            16개의 배열에 데이터를 저장하고 검색할 떄 O(n)
            16개의 데이터 저장공간을 가진 위의 해쉬테이블에 데이터를 저장하고, 검색할 떄 O(1)

'''

