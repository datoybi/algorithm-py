# 맞았습니다!
import sys

str1, answer = list('CAMBRIDGE'), ''
word = sys.stdin.readline().strip()

for i in word:
    flag = False
    for j in str1:
        if i == j: # 같으면 flag를 true로 두어서 더하지말기
            flag = True
            break
    if flag == False:
        answer += i 

print(answer)
        
