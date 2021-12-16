# 어우 복잡해서 반례 찾을 엄두도 안나서 다른 사람 코드 봤는데 엄청 간결해서 놀랐다. 
# 담에 또 풀어보기로 하자...

import sys
input = sys.stdin.readline # 이렇게도 사용하는군..

N, T = map(int, input().split())
d = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 첫번째 원소가 오른쪽(x)이고 두번째 원소가 왼쪽이다.(y)
i = X = Y = 0
li = [0]

for _ in range(N):
    time, s = input().split()
    time = int(time)
    t = time - li[-1]
    li.append(time)
    x, y = d[i][0], d[i][1] 
    X += t * x # 오른쪽에 할당
    Y += t * y # 왼쪽에 할당
    i += 1 if s == 'right' else -1 # right면 i++ 하고 left면 i--하기
    i = i % 4
    # print('x : ' , x , ' , ' , 'y : ' , y)
    # print('X : ' , X , ' , ' , 'Y : ' , Y)
    # print('i : ' , i)
    # print('t : ' , t)
    # print('li : ' , li)

t = T - li[-1]
x, y = d[i][0], d[i][1]
X += t * x
Y += t * y
print(X, Y)


























# import sys

# N, total = list(map(int, sys.stdin.readline().split()))
# direction = 'x+'
# now_x, now_y = 0, 0
# lst = list()

# for _ in range(N):
#     T, S = list(map(str, sys.stdin.readline().split()))
#     lst.append([int(T), S])

# total_val = 0
# if N == 0:
#     print(total, 0)
#     exit(0)

# for i in range(len(lst)):
#     print(direction,',',lst[i][1], '(', now_x, ',', now_y ,')')
#     # right
#     if direction == 'x+' and lst[i][1] == 'right':
#         if i == 0:
#             value = now_x + lst[i][0]
#         else:
#             value = lst[i][0]-lst[i-1][0]
#         now_x = value
#         direction = 'y-'
#     elif direction == 'y-' and lst[i][1] == 'right':
#         value = lst[i][0]-lst[i-1][0]
#         now_y = now_y-value
#         direction =  'x-'
#     elif direction == 'x-' and lst[i][1] == 'right':
#         value = lst[i][0]-lst[i-1][0]
#         now_x = now_x-value
#         direction =  'y+'
#     elif direction == 'y+' and lst[i][1] == 'right':
#         value = lst[i][0]-lst[i-1][0]
#         now_y = value
#         direction =  'x+'

#     # left
#     elif direction == 'x+' and lst[i][1] == 'left': 
#         if i == 0:
#             value = now_x + lst[i][0]
#         else:
#             value = lst[i][0]-lst[i-1][0]
#         now_x = value
#         direction = 'y+'
#     elif direction == 'y-' and lst[i][1] == 'left':
#         value = lst[i][0]-lst[i-1][0]
#         now_y = now_y - value
#         direction =  'x+'
#     elif direction == 'x-' and lst[i][1] == 'left':
#         value = lst[i][0]-lst[i-1][0]
#         now_x = now_x - value
#         direction =  'y-'
#     elif direction == 'y+' and lst[i][1] == 'left':
#         value = lst[i][0]-lst[i-1][0]
#         now_y = value
#         direction =  'x-'

#     print(direction, '(', now_x, ',', now_y ,')')
#     total_val += abs(value)

# if direction == 'y-':
#     print(now_x, now_y-(total - total_val))
# if direction == 'x-':
#     print(now_x-(total - total_val), now_y)
# if direction == 'y+':
#     print(now_x, now_y + (total - total_val))
# if direction == 'x+':
#     print(now_x + total - total_val, now_y)
