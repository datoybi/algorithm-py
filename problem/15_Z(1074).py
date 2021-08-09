'''
    제목 : Z
    난이도 : 중
    유형 : 재귀 함수
    시간 : 40분
'''

# n, r, c = map(int, input().split(' '))
# num = 0
# array = [[0]*2*n for i in range(2*n)]
# count = n

# for i in array:
#     for j in i :
#         print(j, end='')
#     print()

# while(count):
#     if count <= 1:
#         break
#     make_array(num)


#     def make_array(num):
#         for j in range(2):
#             for z in range(2):
#                 print('j , ' , j , ' z , ', z , ' num , ' , num)
#                 array[j][z] = num
#                 num+=1
        


# # for i in range(n):
# #     for j in range(2):
# #         for z in range(2):
# #             print('j , ' , j , ' z , ', z , ' num , ' , num)
# #             array[j][z] = num
# #             num+=1
  
# for i in array:
#     for j in i :
#         print(j, end=' ')
#     print()

def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1 
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
    solve(n / 2, x ,y)
    solve(n / 2, x, y + n / 2)
    solve(n / 2, x + n / 2, y)
    solve(n / 2, x + n / 2, y + n / 2)

result = 0
N, X, Y = map(int, input().split(' '))
solve(2 ** N, 0, 0)