# n, k = map(int, input().split())
# data = ['?'] * n
# idx = 0
# check = True

# print(data)
# for i in range(k):
#     num, alphabet = input().split()
#     idx = (idx + int(num)) % n
#     if data[idx] != '?':
#         if data[idx] == alphabet:
#             continue
#         check = False
#     else:
#         data[idx] = alphabet

# print(data, check)

# for i in range(n):
#     if data[i] == '?':
#         continue
#     for j in range(i + 1, n):
#         if data[i] == data[j]:
#             check = False
#             break

# print(data)

# if check:
#     for _ in range(n):
#         print(data[idx], end='')
#         idx = (idx - 1) % n
# else:
#     print('!')


a,b = list(map(int, input().split()))

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
