''''
abbcccddddeeeee
eddcccbbbbaaaaa

'''

import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# zero_list = [0 for _ in range(130)]

# # print(str1, str2, zero_list)

# # print(ord('a'))
# for i in range(len(str1)):
#     # print(ord(str1[i]))
#     zero_list[ord(str1[i])] += 1

# print(zero_list)

# for i in range(len(str2)):
#     zero_list[ord(str2[i])] -= 1

# print(zero_list)

# for i in range(len(zero_list)):
count = 0

for i in range(len(str1)):
    if str1[i] in str2:
        # print(str1[i] in str2, str1[i], count)
        count += 1
        str1 = str1.replace(str1[i], '')
        str2 = str2.replace(str2[i], '')

print(str1, str2)
# print(abs(len(str1)+len(str2)-count*2))