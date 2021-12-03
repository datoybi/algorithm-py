'''
    맞았습니다!
    
    누가 먼저 시작할지 순서 정하기
    먼저 시작하는 사람이 가장 첫 글자 말하기
    두사람이 번갈아가며 다음글자 말하기 
    이전 사람이 가장 마지막 글자를 말했다면 자신의 차례에 가장 첫 글자 말하기
    
'''

import sys

for _ in range(int(sys.stdin.readline())):
    word = sys.stdin.readline().rstrip()
    A, B, tmp_A, tmp_B = '', '', '', ''
    i, turn = 0, 0

    if len(word) % 2 == 0: #길이가 짝수면
        for j in range(len(word)):
            if j % 2 == 0 :
                A += word[j]
            else:
                B += word[j]

    elif len(word) % 2 == 1: # 길이가 홀수면  
        for j in range(len(word)):
            if j % 2 == 0 :
                tmp_A += word[j]
            else:
                tmp_B += word[j]
            A = tmp_A+tmp_B
            B = tmp_B+tmp_A

    print(A)
    print(B)
    
    