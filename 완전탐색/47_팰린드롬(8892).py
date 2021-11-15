'''
맞았습니다!
앞이나 뒤에서 읽어도 항상 같은 단어
civic, radar, rotor, madam

두단어를 합친 팰린드롬

k(1 ≤ k ≤ 100)
'''

import sys

# 입력
for _ in range(int(sys.stdin.readline())):
    word_lst, ans = list(), ''

    for _ in range(int(sys.stdin.readline())):
        word_lst.append(sys.stdin.readline().strip())

    # 문자열 합치기
    for i in range(len(word_lst)):
        for j in range(len(word_lst)):
            if i == j : continue # 같으면 건너뛰기
            tmp = word_lst[i] + word_lst[j]
            if tmp == tmp[::-1]: # 팰린드롬인지 확인
                ans = tmp
                break      
    if ans:
        print(ans)
    else:
        print(0)





    