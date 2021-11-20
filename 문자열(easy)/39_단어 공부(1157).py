# 맞았습니다!
import sys

word = sys.stdin.readline().rstrip()
lst = [0 for _ in range(123)]

for i in range(len(word)):
    lst[ord(word[i].upper())] += 1 #모든 단어를 리스트에 넣기

if lst.count(max(lst)) != 1: # max가 여러개이면
    print('?')
else:
    for i in range(len(lst)):
        if lst[i] == max(lst):
            print(chr(i))

