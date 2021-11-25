'''
맞았습니다!

    (, [ 가 들어오면 끝에 계속 덧붙여 쌓임
    만약에 ),] 들어오면 맨 끝에 것과 비교를 해서 삭제
    여기서 만약 ]이게 와야하는데 )이게 오면 break하고 no 


'''

import sys

while True:
    sentence = list(sys.stdin.readline().rstrip())
    front, flag = list(), True

    if sentence[0] == '.': exit(0) # 입력값이 .일시 나가기

    for i in range(len(sentence)):
        if flag == False: break
        # print('front : ' , front)

        if sentence[i] == '(' or sentence[i] == '[':
            front.append(sentence[i])
            continue            

        if sentence[i] == ')':
            if len(front) > 0:
                if front[-1] == '(':
                    del front[-1]  
                    continue
                else:
                    flag = False
            else:
                flag = False

        elif sentence[i] == ']':
            if len(front) > 0:
                if front[-1] == '[':
                    del front[-1]  
                    continue
                else:
                    flag = False
            else:
                flag = False

    if len(front) == 0 and flag == True:
        print('yes')
    else:
        print('no')


    