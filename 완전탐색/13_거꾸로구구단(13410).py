'''
맞았습니다!
'''

N, K, lst = map(int, input().split(' ')), list()

for i in range (1, K+1): #1~9
    temp = str(i*N)
    temp = temp[::-1] # string 뒤집기
    lst.append(int(temp))

print(max(lst))
