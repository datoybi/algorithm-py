# 맞았습니다!
# import sys

lst = list()
for _ in range(int(sys.stdin.readline())):
    lst.append(int(sys.stdin.readline()))

height = lst[-1]
count = 1

for i in range(len(lst)-1, -1, -1):
    if height < lst[i]:
        height = lst[i]
        count += 1

print(count)