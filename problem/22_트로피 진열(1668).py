'''
    제목 : 트로피 진열
    난이도 : 하
    유형 : 탐색
    시간 : 20분


'''

n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

# print(array)

left = 1
right = 1
# print(left , right)

for i in range(0, len(array)-1):
    if array[i] <= array[i+1]:
        left += 1

for i in range(len(array)-1, 0, -1):
    if array[i] <= array[i-1]:
        right += 1
    # print(i, i-1)

print(left)
print(right)
