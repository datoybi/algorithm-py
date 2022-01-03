# 맞았습니다!

import sys

while True:
    zero = 0
    n = list(map(int, sys.stdin.readline().split()))
    if n[0] == 0: break
    del n[0]
    n.sort()
    num1, num2 = [], []
    for i in range(len(n)):
        if n[i] == 0:
            zero += 1
            continue
        if i % 2 == 0: 
            num1.append(str(n[i]))
        else:
            num2.append(str(n[i]))

    # num1, num2 크기 비교를 위해
    r1, r2 = '', ''
    for i in num1:
        r1 += i
    for i in num2:
        r2 += i

    for i in range(zero): # 0 넣어주기
        if len(num1) > len(num2): 
            num2.insert(1, '0')
        elif len(num1) < len(num2):
            num1.insert(1, '0')
        elif r1 > r2:
            num2.insert(1, '0')
        elif r1 > r2:
            num1.insert(1, '0')
        else:
            if i % 2 == 0:
                num1.insert(1, '0')
            else:
                num2.insert(1, '0')
    # 출력
    r1, r2 = '', ''
    for i in num1:
        r1 += i
    for i in num2:
        r2 += i

    print(int(r1)+int(r2))
    

# 괜찮은 정해 같아서 가져옴
# while True:
#     num = list(map(int, input().split()))
#     if num[0] == 0:
#         break
#     else:
#         n = num[0]
#         num = num[1:]
#         num.sort()
#         small = list(i for i in num if i!=0)[0:2]

#         num.remove(small[0])
#         num.remove(small[1])

#         odd = str(small[0])
#         even = str(small[1])
        
#         for i in range(0,len(num),2):
#             odd = odd + str(num[i])
#         for j in range(1,len(num),2):
#             even = even + str(num[j])


#         print(int(even)+int(odd))
