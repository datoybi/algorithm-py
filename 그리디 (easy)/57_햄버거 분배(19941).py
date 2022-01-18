'''
맞았습니다!
사람들은 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있다

8 3
PPHHHHPP
4

6 2
HPPPHH
3
'''

# import sys

# N, K = list(map(int, sys.stdin.readline().split()))
# lst = list(sys.stdin.readline().rstrip())
# cnt = 0

# for i in range(N):
#     if lst[i] == 'P':
#         if i-K < 0:
#             s = 0
#         else:
#             s = i-K
#         if i+K < N:
#             b = i+K
#         else:
#             b = N-1
#         tmp = lst[s:b+1]
#         for j in range(len(tmp)):
#             if tmp[j] == 'H':
#                 cnt += 1
#                 lst[i] = 'Z'
#                 lst[s+j] = 'Z'
#                 break            
# print(cnt)

# 멋진 다른 답 
n, k = map(int, input().split())
lst = list(input())
cnt = 0

for i in range(len(lst)):
    if lst[i] == 'P':
        for j in range(max(0, i-k), min(n, i+k+1)):
            if lst[j] == 'H':
                lst[j] = 'eat'
                cnt += 1
                break
print(cnt)