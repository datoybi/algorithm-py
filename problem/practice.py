test_case = int(input())
# left = []
# right = []

# for i in range(test_case):
#     data.append(input());

# print(data)

for j in range(test_case):
    data = input()
    left = []
    right = []

    for i in data:
        # print('left : ' , left, ' , right : ' , right)
        # print(data[i])
        if i == '<':
            if left:
                right.append(left.pop())
                # left.pop()
        elif i == '>':
            if right:
                left.append(right.pop())
                # right.pop()
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.append(left)

    print(''.join(left))
# print('right : ' , right)