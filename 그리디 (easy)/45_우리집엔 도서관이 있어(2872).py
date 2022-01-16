'''
맞았습니다!
시간초과 떄문에 애먹었다..ㅠㅠ

'''

import sys

lst, N = list(), int(sys.stdin.readline())
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

cnt = 0
num = max(lst)

for i in range(N-1,-1,-1):
    if num == lst[i]:
        num -= 1
        cnt += 1
print(N-cnt)


# 시간초과 ..
# index들을 찾는 것과 remove, insert가 별로 효율적이지 않은것 같다
# import sys

# lst, N = list(), int(sys.stdin.readline())
# for _ in range(N):
#     lst.append(int(sys.stdin.readline()))

# cnt = 0
# num = max(lst)-1

# for _ in range(N):
#     if num == 0: break
#     if lst.index(num+1) > lst.index(num):
#         num -= 1
#     else:
#         lst.remove(num)
#         lst.insert(0, num)
#         num -= 1
#         cnt += 1

# print(cnt)



# # 시간초과 ㅠㅠ
# import sys

# lst, N = list(), int(sys.stdin.readline())
# for _ in range(N):
#     lst.append(int(sys.stdin.readline()))

# cnt = 0
# num = max(lst)-1

# while True:
#     is_sorted = False
#     is_sorted = all(x<y for x, y in zip(lst[:-1], lst[1:]))
#     if is_sorted == True:
#         break
#     idx = lst.index(num)
#     if lst.index(num+1) > idx:
#         num -= 1
#     else:
#         del lst[idx]
#         lst.insert(0, num)
#         num -= 1
#         cnt += 1

# print(cnt)



# import sys

# lst, N = list(), int(sys.stdin.readline())
# for _ in range(N):
#     lst.append(int(sys.stdin.readline()))

# cnt = 0
# i = 0
# for _ in range(10):
#     flag = True
#     i = i % N
#     for j in range(1, len(lst)):
#         if lst[j-1] > lst[j]:
#             flag = False
#     if flag == True:
#         break
            
#     if lst[i] == N:
#         if lst[(i+1):] == []:
#             for j in range(1, len(lst)):
#                 if lst[j-1] > lst[j]:
#                     lst[j-1], lst[j] = lst[j], lst[j-1]
#                     cnt += 1
#         else:
#             value = max(lst[(i+1):])
#             lst.remove(value)
#             lst.insert(0, value)
#             cnt += 1
#     i += 1

# print(cnt)
# # print(lst)