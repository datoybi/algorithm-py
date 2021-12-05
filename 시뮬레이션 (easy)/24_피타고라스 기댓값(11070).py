'''
맞았습니다! 
문제이해가 쪼오금 힘들었었다. 
각각의 팀의 실점과 득점을 구하여 기댓값을 각각 구한뒤,
그 기댓값중 최댓값 최솟값을 구하면 되는 문제.

1 13 13
2 26 10
3 8 24
'''

import sys, math

for _ in range(int(sys.stdin.readline())):
    n, m = list(map(int, sys.stdin.readline().split()))
    game = list()
    result = list()

    for i in range(n+1):
        game.append([0, 0])

    for i in range(m):
        a, b, p, q = list(map(int, sys.stdin.readline().split()))
        # print(a, b, p, q)
        game[a][0] += p
        game[a][1] += q
        game[b][0] += q
        game[b][1] += p
        
    for i in range(1, len(game)):
        if game[i][0] == 0 and game[i][1] == 0: 
            w = 0
        else:
            w = math.trunc((game[i][0]**2 / (game[i][0]**2 + game[i][1]**2))*1000)
            # print(result)
        result.append(w)

    print(max(result))
    print(min(result))



