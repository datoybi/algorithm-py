# 맞았습니다! 
import sys

c_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = sys.stdin.readline().rstrip()
i, count = 0, 0 # word 수, 카운트 수

while True:
    flag = False

    for j in range(len(c_lst)):
        length = len(c_lst[j]) + i
        # print(i, length, count, word[i:length])

        if i >= len(word): # word 길이보다 같거나 크면 나가기
            print(count)
            exit(0)

        if c_lst[j] == word[i:length]:
            flag = True
            break
        
    if flag == True:
        i = length
        count += 1
    else:
        i += 1
        count += 1

