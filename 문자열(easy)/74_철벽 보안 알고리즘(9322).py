'''
맞았습니다!
문제 풀이보다 문제 이해가 더 어려운 문제였다.
뭔말이야,, 

1공개키는 최대 한번만 사용된 단어들로 구성 
2공개키는 제1 공개키의 단어들을 재배치하여 만들어짐

평문 - 여러단어긴 한데 각 단어들은 중복이 가능
암호문 - 2 공개키를 만든 규칙의 반대로 재배치

'''

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    key1, key2 = list(map(str, sys.stdin.readline().split())), list(map(str, sys.stdin.readline().split()))
    plaintext = list(map(str, sys.stdin.readline().split()))
    rule = list()

    for i in range(len(key1)):
        for j in range(len(key2)):
            if key1[i] == key2[j]:
                rule.append(j)
                continue
    
    for i in range(len(plaintext)):
        print(plaintext[rule[i]], end=' ')

