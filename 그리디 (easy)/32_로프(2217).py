'''
k개의 로프를 사용하여 중량이 w인 물체
w/k 만큼의 중량

최대중량 구하기

정수 N
버틸 수 있는 최대 중량

k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
이 말이 왜 !!! rope[N] *N번째자리일까??ㅜㅜㅜ 담에 풀어보자 ㅠ

https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-2217%EB%B2%88-%EB%A1%9C%ED%94%84-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
'''

import sys

rope = list()
for _ in range(int(sys.stdin.readline())):
    rope.append(int(sys.stdin.readline()))

result = list()
rope.sort(reverse=True)

for i in range(len(rope)):
    result.append(rope[i] * (i+1))
    
print(max(result))
print(result)


# 시간초과

# import sys

# rope = list()
# for _ in range(int(sys.stdin.readline())):
#     rope.append(int(sys.stdin.readline()))

# rope.sort(reverse=True)
# result = 0
# for j in range(1, len(rope)+1):
#     result = max(result, min(rope[0:j]) * j)
#     print(rope[0:j], min(rope[0:j]) * j)
    
# print(result)