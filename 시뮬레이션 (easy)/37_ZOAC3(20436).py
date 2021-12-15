'''
맞았습니다!
    sl, sr 처음 손가락들의 위치
    문자열 (최대 100자)

'''

import sys
# 자음 모음
left = {'q': [0,0], 'w': [0,1], 'e': [0,2], 'r': [0,3], 't': [0,4], 
        'a': [1,0], 's': [1,1], 'd': [1,2], 'f': [1,3], 'g': [1,4], 
        'z': [2,0], 'x': [2,1], 'c': [2,2], 'v': [2,3]}
right = {'y': [5,5], 'u': [5,6], 'i': [5,7], 'o': [5,8], 'p': [5,9], 
        'h': [6,5], 'j': [6,6], 'k': [6,7], 'l': [6,8],
        'b': [7,4], 'n': [7,5], 'm': [7,6]}

sl, sr = list(map(str, sys.stdin.readline().split()))
word = list(sys.stdin.readline().rstrip())
time = 0

for i in range(len(word)):
    time += 1

    if word[i] in left:
        time += abs(left[sl][0] - left[word[i]][0]) + abs(left[sl][1] - left[word[i]][1])
        sl = word[i]
    else:
        time += abs(right[sr][0] - right[word[i]][0]) + abs(right[sr][1] - right[word[i]][1])
        sr = word[i]

print(time)