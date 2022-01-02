'''
맞았습니다!
UCPPC
'''

import sys

sentence = list(sys.stdin.readline())
lst, answer = [], ''
ucpc = ['U', 'C', 'P', 'C']

for i in sentence:
    if ord(i) == 85 or ord(i) == 80 or ord(i) == 67:
        lst.append(i)

idx = 0
for i in range(len(lst)):
    if idx == 4: break
    if ucpc[idx] == lst[i]:
        idx += 1
        answer += lst[i]

if 'UCPC' == answer:
    print('I love UCPC')
else:
    print('I hate UCPC')

# print(answer)  

