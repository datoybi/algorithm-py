'''
A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.

8
ABCD
A
AB
ABC
145C
A910
Z321
ABCDE
'''

import sys

lst = list()

for _ in range(int(sys.stdin.readline())):
    lst.append(sys.stdin.readline().rstrip())

lst.sort(key=len) # 짧은 길이부터 정렬
print(lst)

length = lst[0]
result = list()
i = 0

while True:
    if len(lst[i]) < len(lst[i+1]):
        result.append(lst[i])
        i += 1
    else:
        while True:
            print(lst[i:])
            if lst[i] lst[i+1]


        i += 1
    if i >= len(lst)-1: break

print(result)


# for i in range(len(lst)):
#     for j in range (i+1, len(lst)):
#         if len(lst[i]) >= length:

#             print(lst[i], lst[j])
