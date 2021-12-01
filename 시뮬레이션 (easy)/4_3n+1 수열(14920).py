'''
맞았습니다!


'''
############################## 간결버전 

import sys

num = int(sys.stdin.readline())
count = 1

while num!= 1:
    if num % 2 == 0: # 짝수면
        num = num // 2
    else:
        num = 3 * num + 1  
    count += 1
print(count)

##############################


# def C(n):
#     if n % 2 == 0: # 짝수면
#         n = n // 2
#     else:
#         n = 3 * n + 1  
#     return n

# import sys

# num = int(sys.stdin.readline())
# count = 1

# if num == 1: 
#     print('1')
#     exit(0)

# while True:
#     if C(num) == 1:
#         count += 1
#         print(count)
#         break
#     else:
#         num = C(num)
#         count += 1


# 뭔가 더 짧은 코드가 있을것만 같아서 찾아봤는데 
# 엄청나게 짧은 코드를 발견했다.

# n=int(input());
# c=1
# while n!=1:
# 	if n%2==1:n=n*3+1
# 	else:n//=2
# 	c+=1
# print(c)
