'''
 (1 ≤ N ≤ M ≤ 5000)

87 104
14
989 1022
0
22 25
3
1234 1234
1

이 문제는 특이하게 입력의 끝을 EOF 시그널로 판단하므로 try-except문을 이용한다. 
(백준 문제를 풀다보면 가끔 입력이 이와 같은 문제를 만날 수 있으니 알아두자)
eof가 뭔지는 잘 모르겠으나 계속 실행할 수 있는 형태로 만들어야해서 try except 사용함

'''
import sys

while True:
    try:
        N,M = map(int, sys.stdin.readline().split()) # N, M 입력
        count = 0
        for i in range(N, M+1):
            flag, tmp = False, list(str(i))
            for j in range(len(tmp)):
                if tmp[j] in tmp[j+1:]: # 중복 판별
                    flag = True
                    break

            if flag == False:
                count +=1
                
        print(count)
    except:
        break