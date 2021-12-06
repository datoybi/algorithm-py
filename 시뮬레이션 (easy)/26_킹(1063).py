
import sys

king, stone, N = list(map(str, sys.stdin.readline().split()))
king, stone = list(king), list(stone)

for _ in range(int(N)):
    move = sys.stdin.readline().rstrip()
    print('king : ' , king, ' , ', 'stone : ' , stone)

    if move == 'R': # 한칸 오른쪽
        if ord(king[0])+2 == ord('I') and king[1] == stone[1]:
            continue
        if ord(king[0])+1 < ord('I'):
            king[0] = chr(ord(king[0])+1)
            if king == stone and ord(stone[0])+1 < ord('I'):
                stone[0] =chr(ord(stone[0])+1)
        else:
            continue
    elif move == 'L': # 한칸 왼쪽
        if ord(king[0])-2 == ord('A') and king[1] == stone[1]:
            continue
        if ord(king[0])-1 > ord('A'):
            king[0] = chr(ord(king[0])-1)
            if king == stone and ord(stone[0])-1 < ord('A'):
                stone[0] = chr(ord(stone[0])-1)
        else:
            continue
    elif move == 'B': # 한칸 아래로
        if int(king[1])-2 == 0 and king[0] == stone[0]:
            continue
        if int(king[1])-1 > 0 :
                king[1] = str(int(king[1])-1)
                if king == stone and int(stone[1])-1 > 0:
                    stone[1] = str(int(stone[1])-1)
        else:
            continue
    elif move == 'T': # 한칸 위로
        if int(king[1])+2 == 9 and king[0] == stone[0]:
            continue
        if int(king[1])+1 < 9 :
                king[1] = str(int(king[1])+1)
                if king == stone and int(stone[1])+1 < 9:
                    stone[1] = str(int(stone[1])+1)
        else:
            continue
    elif move == 'RT': # 오른쪽 위 대각선으로
        # if ord(king[0])+1 == ord('H') and ord(stone[0]) == and int(stone[1]) == 8: # 여기 하는 중 !
            king[0] = chr(ord(king[0])+1)
            king[1] = str(int(king[1])+1)
            if king == stone and ord(stone[0])+1 < ord('I') and int(stone[1])+1 < 9:
                stone[0] =chr(ord(stone[0])+1)
                stone[1] = str(int(stone[1])+1)
        else:
            continue
    elif move == 'LT': # 완쪽 위 대각선으로
        if ord(king[0])-1 > ord('A') and int(king[1])+1 < 9:
            king[0] = chr(ord(king[0])-1)
            king[1] = str(int(king[1])+1)
            if king == stone and ord(stone[0])-1 < ord('A') and int(stone[1])+1 < 9:
                stone[0] = chr(ord(stone[0])-1)
                stone[1] = str(int(stone[1])+1)
        else:
            continue
    elif move == 'RB': # 오른쪽 아래 대각선으로
        if ord(king[0])+1 < ord('I') and int(king[1])-1 > 0 and ord(stone[0])+1 < ord('I') and int(stone[1])-1 > 0:
            king[0] = chr(ord(king[0])+1)
            king[1] = str(int(king[1])-1)
            print(ord(king[0])+1, int(king[1])-1)
            if king == stone:
                if ord(stone[0])+1 < ord('I') and int(stone[1])-1 > 0:
                    stone[0] = chr(ord(stone[0])+1)
                    stone[1] = str(int(stone[1])-1)
        else:
            continue
    elif move == 'LB': # 왼쪽 아래 대각선으로
        if ord(king[0])-1 > ord('A') and int(king[1])-1 < 0:
            print(ord(king[0]))
            king[0] = chr(ord(king[0])-1)
            king[1] = str(int(king[1])-1)
            if king == stone and ord(stone[0])-1 < ord('A') and int(stone[1])-1 < 0:
                stone[0] = chr(ord(stone[0])-1)
                stone[1] = str(int(stone[1])-1)
        else:
            continue

print(f'{king[0]}{king[1]}\n{stone[0]}{stone[1]}')
