# 맞았습니다!
# 딕셔너리가 엔로그고 리스트는 엔 이라고 한다. 더 빠르다

import sys

dictionary = dict()

for _ in range(int(sys.stdin.readline())):
    name, exist = sys.stdin.readline().split()
    # print(name, exist)

    if exist == 'enter':
        dictionary[name] = 'enter'
    elif exist == 'leave':
        del dictionary[name]

dictionary = sorted(dictionary.items(), reverse=True)

for key in dictionary:
    print(key[0])
