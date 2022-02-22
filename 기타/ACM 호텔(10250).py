'''
호텔 층수, 각 층의 방 수, 몇 번째 손님인지
6 12 10
402
1
6 12 10

1
1 11 11
111 
1011

2 1 2
201
'''

for _ in range(int(input())):
    H, W, N = map(int, input().split())
    hotel = [[0 for _ in range(W+1)] for _ in range(H+1)]
    
    cnt = 1
    result = [0, 0]
    for i in range(1, W+1):
        for j in range(1, H+1):
            hotel[j][i] = cnt
            if cnt == N:
                result = [j, i]
            cnt += 1

    if result[1] < 10:
        print(f'{result[0]}0{result[1]}')
    else:
        print(f'{result[0]}{result[1]}')
    