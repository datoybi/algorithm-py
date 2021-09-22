"""
    제목 : SHA-256
    난이도 : 하
    유형 : 해시, 구현
    시간 : 15분
    느낀점 : 보고하지말고 이제 외우기
"""

# 내코드
# import hashlib

# s = input().encode()

# sha_data = hashlib.sha256()
# sha_data.update(s)
# hash_dig = sha_data.hexdigest()
# print(hash_dig)

# 해답코드
# 1.hashlib의 sha256 함수를 이용하면 sha256 해시를 구할 수 있습니다.
# 2.hashlib.sha256(문자열 바이트 객체) hexdigest(): 해시 결과 문자열

import hashlib

input_data = input()
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result)