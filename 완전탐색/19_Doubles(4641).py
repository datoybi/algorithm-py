'''
맞았습니다!
'''
lst = list()

while(True):
    count = 0
    lst = list(map(int, input().split()))
    if lst[0] == -1:
        exit(0)
    for i in lst:
        for j in range(len(lst)):
            if i*2 == lst[j] and i != 0:
                count += 1
    print(count)