# N = list(input())
# result = 0

test = '216'
test_list = list(test)
# result = 0
# print(test_list)

# for i in test_list:
#     result += int(i)
# result + int(test)


# print(result)

for i in range(1, 1000):
    result = 0
    i_lst = list(str(i))
    # print(i_lst)
    # i_lst[0:]
    result += sum(i_lst[0:]) # 여기서 str로 선언했기 때문에 int로 형변환 후 슬라이싱을 진행해야 할 것 같다 =.
    
    # for j in i_lst:
    #     result += j
        
    # if result == 216:
    #     print('216')



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
