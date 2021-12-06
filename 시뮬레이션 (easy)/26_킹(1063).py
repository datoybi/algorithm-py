# 맞았습니다!
# 
# 
# 쉬워보였는데 은근 까다로운 문제였다. 
# 처음에는 생각없이 문제 따라서 풀었는데 점점 꼬이고 이해하기도 어려워서 두번째 시도를 했다.
# 두번째에는 문자를 사용하지 않고 숫자로 했으며 튜플을 사용하여 계산부분을 따로 뺐다.
# 까다로웠던게.. 
# A1 H8 1
# T
# 여기서는 A2 H8이 정답인데(H8아 떨어졌으나 A1이 움직였다.) 나는 떨어지면 무조건 RESET이라고 생각했는데 아니였다.
# B5 A5 1
# L 의 정답은 B5, A5인데 이때는 둘 다 떨어져서 리셋이 되었다.
# 그러니까 킹이 돌을 밀어서 떨어지면 리셋이고 
# 킹이 밀지 않았고, 킹은 리밋이 아니면서 돌이 리밋이면 킹만 카운트를 해야한다. 말이 참 어렵다.
# 오늘 회사에서 부터 하루종일 이 문제를 붙들고 있었는데 맞았습니다!를 봐서 넘 기분이 조타


# 맞왜틀!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
B5 A5 1
L

B5
A5

A1 H8 1
T

A2
H8
'''
import sys

king, stone, N = list(map(str, sys.stdin.readline().split()))
king, stone = [ord(king[0]), int(king[1])], [ord(stone[0]), int(stone[1])]

for _ in range(int(N)):
    move = sys.stdin.readline().rstrip()
    calculate = (0, 0)
    # print('king : ' , chr(king[0]), king[1],  ' , ', 'stone : ' , chr(stone[0]), stone[1])

    if move == 'R': # 한칸 오른쪽
        calculate = (1, 0)
    elif move == 'L': # 한칸 왼쪽
        calculate = (-1, 0)
    elif move == 'B': # 한칸 아래로
        calculate = (0, -1)
    elif move == 'T': # 한칸 위로
        calculate = (0, 1)
    elif move == 'RT': # 오른쪽 위 대각선으로
        calculate = (1, 1)
    elif move == 'LT': # 완쪽 위 대각선으로
        calculate = (-1, 1)
    elif move == 'RB': # 오른쪽 아래 대각선으로
        calculate = (1, -1)
    elif move == 'LB': # 왼쪽 아래 대각선으로
        calculate = (-1, -1)

    # 리밋 계산
    limit_0, limit_1 = 65, 1
    if calculate[0] == 1:
        limit_0 = 72
    elif calculate[0] == -1:
        limit_0 = 65
    if calculate[1] == 1:
        limit_1 = 8
    elif calculate[1] == -1:
        limit_1 = 1
    
    # 계산
    if stone[0] == limit_0 and stone[1] == limit_1 and king[0] + calculate[0] == stone[0] and king[1] + calculate[1] == stone[1]:
        continue
    if king[0] + calculate[0] <= 72 and king[0] + calculate[0] >= 65 and king[1] + calculate[1] < 9 and king[1] + calculate[1] > 0 :
        king[0] = king[0] + calculate[0]
        king[1] = king[1] + calculate[1]
        if stone == king: 
            if stone[0] + calculate[0] <= 72 and stone[0] + calculate[0] >= 65 and stone[1] + calculate[1] < 9 and stone[1] + calculate[1] > 0:
                stone[0] = stone[0] + calculate[0]
                stone[1] = stone[1] + calculate[1]
            else: # 같은데 돌이 범위를 넘었으면 킹은 되돌아오기
                king[0] = king[0] - calculate[0]
                king[1] = king[1] - calculate[1]
    else:
        continue
    

print(f'{chr(king[0])}{king[1]}\n{chr(stone[0])}{stone[1]}')


































# import sys

# king, stone, N = list(map(str, sys.stdin.readline().split()))
# king, stone = list(king), list(stone)

# for _ in range(int(N)):
#     move = sys.stdin.readline().rstrip()
#     print('king : ' , king, ' , ', 'stone : ' , stone)

#     if move == 'R': # 한칸 오른쪽
#         if ord(king[0])+1 == ord('H') and king[1] == stone[1]:
#             continue
#         if ord(king[0])+1 < ord('I'):
#             king[0] = chr(ord(king[0])+1)
#             if king == stone and ord(stone[0])+1 < ord('I'):
#                 stone[0] =chr(ord(stone[0])+1)
#         else:
#             continue
#     elif move == 'L': # 한칸 왼쪽
#         if ord(king[0])-1 == ord('A') and king[1] == stone[1]:
#             continue
#         if ord(king[0])-1 > ord('A'):
#             king[0] = chr(ord(king[0])-1)
#             if king == stone and ord(stone[0]) > ord('A'):
#                 stone[0] = chr(ord(stone[0])-1)
#         else:
#             continue
#     elif move == 'B': # 한칸 아래로
#         if int(king[1])-2 == 0 and king[0] == stone[0]:
#             continue
#         if int(king[1])-1 > 0 :
#                 king[1] = str(int(king[1])-1)
#                 if king == stone and int(stone[1])-1 > 0:
#                     stone[1] = str(int(stone[1])-1)
#         else:
#             continue
#     elif move == 'T': # 한칸 위로
#         if int(king[1])+2 == 9 and king[0] == stone[0]:
#             continue
#         if int(king[1])+1 < 9:
#                 king[1] = str(int(king[1])+1)
#                 if king == stone and int(stone[1])+1 < 9:
#                     stone[1] = str(int(stone[1])+1)
#         else:
#             continue
#     elif move == 'RT': # 오른쪽 위 대각선으로
#         if stone[0] == 'H' and king[0] == 'G' and int(king[1])+1 == int(stone[1]): # 마지막에 돌이 그 위치에 있을 때 처리
#             continue
#         if int(king[1])+1 < 9 and int(king[1])+1 < 9:
#             king[0] = chr(ord(king[0])+1)
#             king[1] = str(int(king[1])+1)
#             if king == stone and ord(stone[0])+1 < ord('I') and int(stone[1])+1 < 9:
#                 stone[0] = chr(ord(stone[0])+1)
#                 stone[1] = str(int(stone[1])+1)
#         else:
#             continue
#     elif move == 'LT': # 완쪽 위 대각선으로
#         if stone[0] == 'A' and king[0] == 'B' and int(king[1])+1 == int(stone[1]): # 마지막에 돌이 그 위치에 있을 때 처리
#             continue
#         if ord(king[0])-1 > ord('A') and int(king[1])+1 < 9:
#             king[0] = chr(ord(king[0])-1)
#             king[1] = str(int(king[1])+1)
#             if king == stone and ord(stone[0]) > ord('A') and int(stone[1])+1 < 9:
#                 stone[0] = chr(ord(stone[0])-1)
#                 stone[1] = str(int(stone[1])+1)
#         else:
#             continue
#     elif move == 'RB': # 오른쪽 아래 대각선으로
#         if king[1] == '2' and stone[1] == '1' and ord(stone[0]) == ord(king[0])+1:
#             continue
#         if ord(king[0])+1 < ord('I') and int(king[1])-1 > 0:
#             king[0] = chr(ord(king[0])+1)
#             king[1] = str(int(king[1])-1)
#             if king == stone:
#                 if ord(stone[0])+1 < ord('I') and int(stone[1])-1 > 0:
#                     stone[0] = chr(ord(stone[0])+1)
#                     stone[1] = str(int(stone[1])-1)
#         else:
#             continue
#     elif move == 'LB': # 왼쪽 아래 대각선으로
#         if king[1] == '2' and stone[1] == '1' and ord(stone[0]) == ord(king[0])+1:
#             continue
#         if ord(king[0])-1 > ord('A') and int(king[1])-1 > 0:
#             king[0] = chr(ord(king[0])-1)
#             king[1] = str(int(king[1])-1)
#             if king == stone and ord(stone[0]) > ord('A') and int(stone[1])-1 > 0:
#                 stone[0] = chr(ord(stone[0])-1)
#                 stone[1] = str(int(stone[1])-1)
#         else:
#             continue

# print(f'{king[0]}{king[1]}\n{stone[0]}{stone[1]}')
