

import sys

variable = list(map(str, sys.stdin.readline().split()))
front = variable[0]
lst = list()
print(front)

for i in range(1, len(variable)):
    lst.append(variable[i][0:len(variable)])

check = ['&', '[]', '*']

print(lst)

# ['int&', 'a*[]&,', 'b,', 'c*;']
# for i in range(1, len(variable)):
#     temp =  variable[0]
#     print(variable[i][1:])
    # print(rev[::-1])


    # for j in range(len(check)):
    #     if check[j] in variable[i]:
