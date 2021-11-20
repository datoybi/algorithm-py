# 맞았습니다!
import sys

while True:
    alphabet = set()
    sentence = sys.stdin.readline().rstrip()
    if sentence == '*': break

    cnt = 26
    for i in sentence:
        alphabet.add(i)
    if ' ' in alphabet: # 공백 포함시 cnt+1
         cnt = 27
   
    if cnt == len(alphabet):
        print('Y')
    else:
        print('N')
