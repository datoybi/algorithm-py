# 맞았습니다!
import sys

count = 0
for _ in range(int(sys.stdin.readline())):
    word = sys.stdin.readline().rstrip()
    zero_lst = [0 for _ in range(123)]
    flag = True

    for i in range(len(word)):
        if zero_lst[ord(word[i])] == 0:
            zero_lst[ord(word[i])] += 1
        elif zero_lst[ord(word[i])] != 0 and word[i-1] == word[i]: # 0이 아니고 값이 중복됐으면 
            zero_lst[ord(word[i])] += 1
        else:
            flag = False

    if flag == True:
        count += 1

print(count)
