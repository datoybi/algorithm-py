'''
azc xyabcxy
1
abc xxbzzz
2
'''

import sys

A,B = sys.stdin.readline().split()
result = len(B)
# print(A, B)

if A in B : # 만약에 A가 B안에 있으면
    print('0')
    exit(0)
else:
    cnt = len(B) - len(A) 
    for i in range(cnt+1):
        diff = 0
        # print(B[0:i] , B[len(B)-cnt+i:])
        tmp = B[0:i] + A + B[len(B)-cnt+i:]
        for j in range(len(tmp)):
            if tmp[j] != B[j]:
                diff += 1
        result = min(result, diff)
    
    print(result)



'''
a = 'xyabcxy' # len 7 4

print(a[len(a)-4:])
print(a[4:])

b = 'xxbzzz' # len 6 3

print(b[len(b)-3:])
print(b[4:])

c = 'aababbc' # 1
print(c[0:1])
print(c[len(c)-1:])

'''