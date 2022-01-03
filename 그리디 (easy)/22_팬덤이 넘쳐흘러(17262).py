import sys

max_val = 0
whole = set()
for _ in range(int(sys.stdin.readline())):
    N, M = list(map(int, sys.stdin.readline().split()))
    check, count = False, 0

    for i in range(N, M+1): # whole 안에 있으면
        if i in whole:
            check = True

    if check == False and len(whole) == 0: # 맨처음
        max_val = M

    if check == False and len(whole) != 0: # 없으면
        print('max : ' , max_val)
        count += N - max_val

    for i in range(N, M+1):
        whole.add(i)
        max_val = M


    print('cnt : ' , count, 'max_val : ' , max_val)

print(count)