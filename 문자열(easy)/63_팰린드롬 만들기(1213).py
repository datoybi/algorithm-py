'''
맞았습니다!
    팰린드롬 규칙 
        문자의 길이가 짝수면 짝수만 있어야함 
        문자의 길이가 홀수면 홀수 1개가 잇어야함
'''


import sys

# 65 90
word = sys.stdin.readline().rstrip()
lst = [0 for _ in range(91)]

for i in range(len(word)):
    lst[ord(word[i])] += 1

odd = 0 # 홀수 갯수 계산
for i in lst:
    if i % 2 != 0:
        odd += 1

if (len(word) % 2 == 0 and odd == 0) or (len(word) % 2 != 0 and odd == 1):
    result, middle = list(), ''

    for i in range(len(lst)-1, 60, -1): # 91~61
        if lst[i] != 0:
            # 만약 홀수면서 1보다 크면 길이만큼 양 옆으로 넣어주고 1개는 odd 에 담아주기
            # 만약 짝수면 양 옆으로 넣어주기 
            # 홀수 odd 가 있으면 중간에 넣어주기
            if lst[i] % 2 != 0: # 홀수면                
                for j in range(1, lst[i], 2):
                    result.insert(0, chr(i))
                    result.append(chr(i))
                middle = chr(i)
                # print(result)
            else: # 짝수면
                for j in range(1, lst[i], 2):
                    result.insert(0, chr(i))
                    result.append(chr(i))
                # print(result)
    if middle:
        result.insert(len(result)//2, middle)

    for i in result: # 출력 
        print(i, end='')

else:
    print("I'm Sorry Hansoo")
