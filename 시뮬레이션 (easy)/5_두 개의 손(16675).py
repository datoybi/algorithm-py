'''    
    맞았습니다!!
    엄청 지저분하게 짠 느낌이다.. 
    아직 시뮬이 익숙치 않아 규칙을 좀 생각했어야 했던 문제다

    내가 생각한 규칙
    둘중 한명은 같은 손을 내밀어야 판별가능

'''
import sys

ML, MR, TL, TR = list(map(str, sys.stdin.readline().split()))

if ML != MR and TL != TR: # 서로 다른 손이면
    print('?')

elif ML == MR and TL != TR: #MS가 같은 손일경우
    compare = ''
    if ML == 'P':
        compare = 'S'
    elif ML == 'S':
        compare = 'R'
    elif ML == 'R':
        compare = 'P'
    if compare == TL or compare == TR:
        print('TK')
    else:
        print('?')

elif TL == TR and ML != MR: #TK가 같은 손일경우
    compare = ''
    if TL == 'P':
        compare = 'S'
    elif TL == 'S':
        compare = 'R'
    elif TL == 'R':
        compare = 'P'
    if compare == ML or compare == MR:
        print('MS')
    else:
        print('?')

else: # 둘다 같은 손일 경우
    if TL == TR == ML == MR:
        print('?')
    else:
        if TL == 'P':
            compare = 'S'
        elif TL == 'S':
            compare = 'R'
        elif TL == 'R':
            compare = 'P'
        if compare == ML or compare == MR:
            print('MS')
        else:
            print('TK')



# 왜 이렇게 짜는지 잘 모르겠지만 간결해서 퍼왔다
ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())
# 가위(S), 보(P), 주먹(R)을 숫자로 표현 => S,P,R = 0,1,2

# 한 사람이 같은 것을 냈을 때, 다른 한사람은 이길 수 있는 가능성이 있다
if ML == MR and (ML+2) % 3 in [TL,TR]:
	print("TK")

elif TL == TR and (TL+2) % 3 in [ML, MR]:
	print("MS")

else:
	print("?")