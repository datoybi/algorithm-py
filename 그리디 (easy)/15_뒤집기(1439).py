'''
맞았습니다!
11001100110011000000
101010101010

'''

import sys
word = sys.stdin.readline().rstrip()
zero, one = 0, 0
past = 'one' if word[0] == '0' else 'zero'

for i in range(len(word)):
    print(zero, one, past)
    if word[i] == '0' and past == 'one':
        zero += 1
        past = 'zero'
    elif word[i] == '1' and past == 'zero':
        one += 1
        past = 'one'

print(min(zero, one))