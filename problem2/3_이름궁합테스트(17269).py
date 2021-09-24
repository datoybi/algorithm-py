# 열삼하 해보려고 했는데 막힘 ㅠ 뭔가 내가 꼬아서 생각하는 것 같기도 하고......
'''
# print(ord('A'))

dic = {
    'A':3,
    'B':2,
    'C':1,
    'D':1
    
        }

first = 'BCD'
second = 'DB'
result = list()

for i in range(len(first)):
    if len(first) > len(second) and len(second) <= i:
        result.append(dic[first[i]]) 
        # print(first[i])
    else:
        result.append(dic[first[i]]) 
        result.append(dic[second[i]]) 
        # print(first[i])
        # print(second[i])

print('\n\n\n\n')

if len(second) > len(first):
    for i in range(len(first), len(second)):
        # print(second[i])
        result.append(dic[second[i]]) 

print(result)

sum = list()
value = 0

for i in range(len(result)-1):
    for j in range(1, -1, len(result)):
        value = result[0] + result[1]
        if value >= 10:
            value -= 10
        sum.append(value)
        del result[0]
    result = []
    result.append(sum)

print(result)

# while len(result) != 1:
#     value = result[0] + result[1]

#     if value >= 10:
#         value -= 10

#     result.append(value)
#     del result[0]
    
#     print('value : ' , value)
#     print('sum : ' , result)
#     print('result : ' , result)     

'''
# 강사 답안
N, M = map(int, input().split())
A, B = input().split()
# print(N, M, A, B)

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
# print(len(alp))

AB = ''
min_len = min(N, M)
for i in range(min_len):
    AB += A[i] +B[i]

AB += A[min_len:] + B[min_len:]
# print(ord('A'))
lst = [alp[ord(i)-ord('A')] for i in AB] # 이건 당최 뭔 뜻?
# print(lst)

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print("{}%".format(lst[0] % 10*10 + lst[1]%10))
