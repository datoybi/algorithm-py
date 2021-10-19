'''
맞았습니다!
'''
n_lst = list(map(int, input().split(' ')))

i = min(n_lst)
while True:
    count = 0
    for num in n_lst:
        if i % num == 0:
            count += 1 
    if count > 2:
        print(i)
        break
    i+=1
    
