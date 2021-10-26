'''
맞았습니다!
'''
str, lst = input(), list()

for i in range (1, len(str)-2):
  for j in range (i+1, len(str)):
    # print(str[0:i], str[i:j], str[j:])
    str1, str2, str3 = str[0:i], str[i:j], str[j:]
    real = str1[::-1] + str2[::-1] + str3[::-1]
    # print(ord(real))

    lst.append(real)
lst.sort()

print(lst[0])