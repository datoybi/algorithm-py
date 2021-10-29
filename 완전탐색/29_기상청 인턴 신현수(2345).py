'''
맞았습니다!

'''

N,M = map(int,input().split())
temparature_lst = list(map(int, input().split()))
max_value = -100*M

for i in range(M, len(temparature_lst)+1):
    # print(i-M, i)
    # print(temparature_lst[i-M:i], sum(temparature_lst[i-M:i]))
    if max_value < sum(temparature_lst[i-M:i]):
        max_value = sum(temparature_lst[i-M:i])
    
print(max_value)
