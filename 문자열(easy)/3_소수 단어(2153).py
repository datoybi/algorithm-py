'''
맞았습니다!
'''

import sys
word = sys.stdin.readline().strip()

answer = 0
for i in range(len(word)):
    if word[i].isupper():
        answer += ord(word[i])-38
    elif word[i].islower():
        answer += ord(word[i])-96
    # print(answer)

# print(answer)
#소수계산만하면됌
for i in range(2,answer-1):
    if answer % i == 0:
        # print(i)
        print("It is not a prime word.")
        exit(0)

print("It is a prime word.")