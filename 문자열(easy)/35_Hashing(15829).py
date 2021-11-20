# 맞았습니다!
# 수학 -.-

# print(1*31**0)
# print( 2*31**1)
# print(3*31**2)

# print(ord('a')-96)
# print(ord('z')-96)

import sys

L = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
sum = 0

for i in range(len(S)):
    sum += (ord(S[i])-96)*(31**i)
    
print(sum % 1234567891)
