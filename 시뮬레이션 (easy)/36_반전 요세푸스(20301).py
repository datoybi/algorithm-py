# 거꾸로 할때 idx 구하는게 어려워서 deque를 배웠다ㅠ 어렵어렵... 
# 다음에 꼭 다시 풀어보기


from collections import deque

N, K, M = map(int, input().split())
queue = deque(range(1, N+1))
i = 0
while queue:
    # 이런방법은 처음 알았다 몫이 양수면 -> 몫이 0,1,2.. 면 시계방향이고
    # 홀수면 반시계방향이다.
    if i//M % 2 == 0: 
        for _ in range(K-1):
            queue.append(queue.popleft()) # 맨 첫번째 원소를 뒤에 붙이기
            print(queue)
    else:
        for _ in range(K):
            queue.appendleft(queue.pop()) # 마지막 원소를 앞에 붙이기
            print(queue)

    i += 1
    print(queue.popleft())








# import sys

# N, K, M = list(map(int, sys.stdin.readline().split())) # N까지의 수를 K만큼 건너뛰고 M번째 때 방향을 돌려가며 삭제
# lst = [i for i in range(1,N+1)]
# result = list()
# print(lst)

# idx = 0
# count = 0
# flag = True # True 시계방향 False 반시계방향
# for _ in range(10):
#     if flag:
#         print(flag)
#         count += 1
#         print('전 idx ' , idx)
#         idx = (idx + K-1) % len(lst)
#         print('후 idx : ' , idx)
#         print('lst[idx] : ' , lst[idx])
#     else:
#         print(flag)
#         count += 1
#         print('전 idx ' , idx)
#         idx -= K
#         if idx < 0:
#             idx = len(lst)+idx    
#         print('후 idx : ' , idx)


#     result.append(lst[idx])
#     del lst[idx]
#     if len(lst) == 0:
#         break
#     if count == M:
#         if flag == True:
#             flag = False
#         else:
#             flag = True
#         count = 0

#     print('result : ' , result)
#     print('lst : ' , lst)

# print(result)  
    
    
    # 이거의 문제점은 뭐가 안에 들어있는지를 모른다는 거
    # idx = (idx + K) % N
    # print('전 idx ' , idx)
    # if idx >= len(lst):
    #     idx -= len(lst)
    # print('후 idx : ' , idx)
    # print('lst[idx] : ' , lst[idx])
    # result.append(lst[idx])
    # print('result : ' , result)
    # print('lst : ' , lst)



# for _ in range(10):
#     # print('idx : ' , idx, ' K : ', K, 'len(lst) : ', len(lst))
#     # n보다 k가 작으니까 여러번 도는 경우의 수는 카운트 안해도됨
#     # idx = (idx + K) % len(lst)-1
#     print('전 idx ' , idx)
#     if idx >= len(lst):
#         idx -= len(lst)
#     print('후 idx : ' , idx)
#     print('lst[idx] : ' , lst[idx])
#     result.append(lst[idx])
#     del lst[idx]
#     print('result : ' , result)
#     print('lst : ' , lst)
    
#     idx += K-1
    
