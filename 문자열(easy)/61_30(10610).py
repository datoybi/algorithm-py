

# 3의 배수는 각 자리 숫자의 합이 3의 배수인 수이다.
# 10의 배수는 일의 자리가 0인 수이다.


import sys, itertools

num = list(sys.stdin.readline().rstrip())
# print(num)
sum = 0
for i in num:
    sum += int(i)
# print(sum)

if '0' not in num or sum % 3 != 0:
    print('-1')
    exit(0)
else:
    lst = list(itertools.permutations(num, len(num)))
    result = 0

    for i in range(len(lst)):
        tmp = int(''.join(lst[i]))
        # print(tmp)

        if tmp % 30 == 0:
            result = max(result, tmp)
            # print(tmp)

    if result == 0:
        print(-1)
    else:
        print(result)




# # 메모리초과 코드 permutations 이게 메모리초과가 난다
# import sys, itertools

# num = list(sys.stdin.readline().rstrip())
# lst = list(itertools.permutations(num, len(num)))
# result = 0

# for i in range(len(lst)):
#     tmp = int(''.join(lst[i]))
#     # print(tmp)

#     if tmp % 30 == 0:
#         result = max(result, tmp)
#         # print(tmp)

# if result == 0:
#     print(-1)
# else:
#     print(result)


