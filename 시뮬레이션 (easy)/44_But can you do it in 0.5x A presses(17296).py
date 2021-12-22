'''
맞 왜 틀 !!@#!@#
4
1 0.5 1 0.5

2

누를 때 1 
'''
import sys

N = int(sys.stdin.readline())
lst = list(map(float, sys.stdin.readline().split()))
press = False
count = 0

for i in lst:
    # print('현재 : ' , i, ' , ' , 'count : ' , count , ' , ' , press)
    while i > 0:
        # print('전 현재 : ' , i, ' , ' , 'count : ' , count , ' , ' , press)
        if press == False: # 버튼이 눌려져 있지 않으면
            count += 1
            i -= 1
        elif press == True: # 버튼이 눌려져 있으면
            i -= 0.5
            while i > 0:
                i -= 1
                count += 1
        #         print('후 현재 : ' , i, ' , ' , 'count : ' , count , ' , ' , press)
        # print('후 현재 : ' , i, ' , ' , 'count : ' , count , ' , ' , press)

    press = True

print(count)




"""

'''
5
0.5 2.5 0 1.5 1
5

4
1 2.5 1.5 2.5

5
3 3 3 3 3

4
3.5 3.5 3.5 3.5
13

5
3 0 0 0 0
3

5
2 2 2 2 10
18

1
100
100


'''
import math
n = int(input())
a = list(map(float, input().split()))

while len(a) > 1 and a[0] == 0 :
    del a[0]

print(math.ceil(a[0]) + sum(int(i) for i in a) - int(a[0]))

"""