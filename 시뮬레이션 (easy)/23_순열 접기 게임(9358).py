'''
맞았습니다!

1
5
2 5 10 3 -4

'''

import sys, math
TC = int(sys.stdin.readline())

for tc in range(1, TC+1):
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    # print(N, lst)
    while True:
        new_lst = list()

        if N == 2: 
            print(f'Case #{tc}: Alice') if lst[0] > lst[1] else print(f'Case #{tc}: Bob') 
            break

        middle = 0
        if len(lst) % 2 == 1:
                middle = lst[len(lst)//2] * 2 # 길이가 홀수면 가운데값 구하기 
                # print(middle)

        for i in range(1, (len(lst)+1)//2):
            # print(lst[i-1], lst[-i])
            new_lst.append(lst[i-1] + lst[-i]) # 끝과 끝 구해서 더해주기

        new_lst.append(middle)
        lst = new_lst
        
        N = math.ceil(N/2) 
        # print(new_lst, N)


