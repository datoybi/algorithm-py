'''    
    R S P R

    R P 0 1
    R R 0 0
    S P 1 0
    S R 0 1

    R R S S

    R S 1 0
    R S 1 0
    S R 0 1
    S R 0 1

    P P S R

    P S 0 1
    P R 1 0
    S P 1 0
    R P 0 1



'''
import sys

lst = list(map(str, sys.stdin.readline().split()))
print(lst)

MS, TK = list(), list()
MS.append(lst[0]) 
MS.append(lst[1]) 

TK.append(lst[2]) 
TK.append(lst[3]) 

print(MS, TK)

win = list()
for i in range(len(lst)):
    tmp = ''
    if lst[i] == 'R':
        tmp = 'P'
    elif lst[i] == 'S':
        tmp = 'R'
    else:
        tmp = 'S'
    win.append(tmp)

print(win)

win_MS, win_TK = list(), list()
win_MS.append(win[0]) 
win_MS.append(win[1]) 

win_TK.append(win[2]) 
win_TK.append(win[3]) 

print(win_MS, win_TK)

for i in range(2):
    if MS[i] in win_TK:
        print('MS : ' , MS[i])
    
    if TK[i] in win_MS:
        print('TK : ' , TK[i])
    