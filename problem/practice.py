# N,M = map(int, input().split(' '))
# arr = list(map(int, input().split(' ')))
# result = 0

# for i in range (len(arr)): # 0~4
#     for j in range (i+1, len(arr)): # 1~4
#         for z in range (j+1, len(arr)): # 2~4
#             temp = arr[i]+arr[j]+arr[z]
#             if temp <= M:
#                 if result < temp:
#                     result = temp

# print(result)