# 맞았습니다!

'''
    반례 
    3
    인 경우 0과 NO가 출력되어야 함
'''
import sys

count = 0
num = sys.stdin.readline().rstrip()

while True:
    sum = 0

    if len(num) > 1:
        count +=1
        for i in range(len(num)):
           sum += int(num[i])
    else:
        answer = ''
        if int(num) % 3 == 0 :
            answer = 'YES'
        else:
            answer = 'NO'
        
        print(count)
        print(answer)
        exit(0)
        
    num = str(sum)
    
    