'''
맞았습니다!

N 라운드
진 사람이 탈락, 이긴 사람이 게임을 계속함 
비긴 경우는 새로 출전한 사람이 승리한 것으로 간주하고
첫판에는 비기는 경우 없이 반드시 승패가 갈린다.
가위 : 1
바위 : 2
보 : 3

N (1 <= N <= 300)
반례 (연속되고 끝나면 count 갱신을 안해주었다)
3
1 2 3
2 3 1

답 : 3
'''

def calculate(team1, team2): # 가위바위보 하면 이긴팀 추출하는 메서드
    winner = 0

    if team1 == team2:
        winner = 3
        return winner

    if team1 == 1:
        if team2 == 3:
            winner = 1
        elif team2 == 2:
            winner = 2

    elif team1 == 2:
        if team2 == 1:
            winner = 1
        elif  team2 == 3:
            winner = 2

    elif team1 == 3:
        if team2 == 2:
            winner = 1
        elif team2 == 1:
            winner = 2

    return winner

import sys
# 입력
N = int(sys.stdin.readline())
team1 = list(map(int, sys.stdin.readline().split()))
team2 = list(map(int, sys.stdin.readline().split()))
tmp = 1
count, old_win = 1, 0

# 연산
for i in range(N):
    winner = calculate(team1[i],team2[i])
    if winner == 3: # 무승부면 새로운 팀이 이김
        if old_win == 1:
            winner = 2
        else:
            winner = 1
    # print('winner : ' , winner, ' old_win : ' , old_win, ' count : ' , count)

    if winner == old_win:
        tmp += 1
    else:
        count = max(count, tmp)
        tmp = 1

    count = max(count, tmp)
    old_win = winner
        
print(count)
    


    
        
