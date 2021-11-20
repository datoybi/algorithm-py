
import sys

num = sys.stdin.readline().rstrip()
flag = False

for i in range(1, len(num)):
    sum1, sum2 = 1, 1 # print(num[0:i], num[i:]) 

    for j in num[0:i]:
        sum1 = int(j)*sum1
    
    for z in num[i:]:
        sum2 = int(z)*sum2
    
    if sum1 == sum2: # 곱이 같으면 flag = True
        flag = True

if flag == True:
    print('YES')
else:
    print('NO')