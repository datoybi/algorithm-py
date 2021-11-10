'''
25 = 5*5 
26 = 5*5 + 1*1
11339 = 3
34567 = 4
'''

# n = int(input())
count = 0
n = 26
count = 0
num = int(n**0.5) # 루트 구하는 공식임다
print(num, n)

while True:
    print(num, n) # 5 26 , 4 1
    if num == 0: break
    if n > 0:
        if n - num < 0: 
             num -= 1
        else:
            count += 1
            n = n - num # n = 1
            num -= 1 # num = 4
    elif n == 0:
        break
    elif n < 0:
        num -= 1            





# lst = list()

# def func(num, n):
#     print(num, n)
#     n = n - num**2 

#     print(n)

#     if n > 0:
#         print('num : ' , num)
#         lst.append(num)
#         func(num-1,n)
#     elif n == 0 :
#         lst.append(num)
#     elif 

    
    
# func(num, n)

# print("lst : " , lst)