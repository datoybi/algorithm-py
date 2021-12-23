'''
    맞았습니다! 
    나의 첫 실버2 맞은 문제.. 조건이 까다로워서 내가 잘 하고있는건가?? 했는데 결국 맞았다. 뿌듯~

    매칭 가능한 방비 없으면 새로운 방 생성하고 입장 
    처음 입장한 플레이어의 레벨을 기준으로 -10 ~ +10까지 입장 가능

    입장 가능한 방이 있으면 입장시킨 후 정원이 모두 찰때까지 대기

    플레이어의 수 p (1~300)
    플레이어의 닉네임 n ()
    플레이어의 레벨 l (1~500)
    방 한개의 정원 m (1~300)

    p, m
    플레이어들이 나열 , 레벨과 닉네임
    
'''
import sys

# 입력
p, m = list(map(int, sys.stdin.readline().split()))
r_range = list() # 방 범위
first = True # 첫번째인지 판별
room = ([[0] for _ in range(300)]) # 최대 300개까지 방 만들기

# 계산
for i in range(p):
    flag = False # room에 들어갔는지 안들어갔는지 판별
    l, n = list(map(str, sys.stdin.readline().split()))
    
    if first == True: # 처음일때 범위에 넣어주기
        r_range.append(l)
        first = False
    
    for j in range(len(r_range)): # 조건들이 맞으면 해당 room에 넣어주기
        if int(r_range[j])-10 <= int(l) and int(r_range[j])+10 >= int(l) and len(room[j]) <= m and flag == False:
            room[j].append((l, n))
            flag = True

    if flag == False: # 들어가지 않았다면 방 생성
        r_range.append(l)
        room[len(r_range)-1].append((l, n))

# print('room : ' , room)
# print('r_range : ' , r_range)

# 출력
for i in range(len(room)):
    room[i].remove(0)
    room[i] = sorted(room[i], key=lambda x:x[1]) # 정렬

    if len(room[i]) == m:
        print("Started!")
        for j in range(0, len(room[i])):
            print(f'{room[i][j][0]} {room[i][j][1]}')

    elif len(room[i]) > 0 :
        print("Waiting!")
        for j in range(0, len(room[i])):
            print(f'{room[i][j][0]} {room[i][j][1]}')

