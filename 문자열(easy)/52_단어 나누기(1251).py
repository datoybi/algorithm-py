# 맞았습니다!

import sys

word = sys.stdin.readline().rstrip()

# print(word)
answer = list()
for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        word1, word2, word3 = word[0:i], word[i:j], word[j:] 
        # print(word[0:i], word[i:j], word[j:])
        answer.append(word1[::-1]+word2[::-1]+word3[::-1]) # 뒤집고 더하기

answer.sort()
print(answer[0])
