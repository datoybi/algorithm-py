# 맞았습니다

N = int(input())
result = 0

for i in range(1, 1000001):
    result = i
    i_lst = list(map(int, str(i)))
    result += sum(i_lst[0:])
    
    if result == N:
        print(i)
        exit(0)

print('0')
    
    # for j in i_lst:
    #     result += j
        
    # if result == 216:
    #     print('216')


# result = 0
# i_lst = list(test)
# result = int(test)
# # print(i_lst)
# # i_lst[0:]
# i_lst = list(map(int, i_lst))
# result += sum(i_lst[0:])
# print(result)

# lst = [1,2,3] # 6+1+2+3 = 12
# print(sum(lst[0:]))
# print(lst[0])
# print(lst[1])
# print(lst[2])

# result += sum(lst[0:])

# for j in lst:
#     result += j

# print(result)





# def aaa(a, i) :
#     result = a[i-1][0] + a[i][1]
#     print(result)
#     # print(a[0][0], a[1][0])
   
# a = [('x0', 'y0'), 
# ('x1', 'y1'),
# ('x2', 'y2'), 
# ('x3', 'y3'),
# ('x4', 'y4'), 
# ('x5', 'y5')]

# for i in range(1, len(a)):
#     # print(i)
#     aaa(a, i)
