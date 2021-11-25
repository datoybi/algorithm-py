'''
맞았습니다!

만약에 ( 가 들어왔을 때 리스트에 저장해두고
리스트에 (가 있을 때 )가 들어오면 기존의 가장 끝 리스트 원소를 삭제


(()()) ((()))
()()()()(()()())()

'''
import sys

for _ in range(int(sys.stdin.readline())):
    ps = list(sys.stdin.readline().rstrip())
    front, flag = list(), True

    for i in range(len(ps)):
        if flag == False: break

        if ps[i] == '(':
            front.append('(')
            continue

        if len(front) != 0 and ps[i] == ')':
            del front[-1]
        else:
            flag = False
    
    if flag == True and len(front) == 0 :
        print('YES')
    else:
        print('NO')


