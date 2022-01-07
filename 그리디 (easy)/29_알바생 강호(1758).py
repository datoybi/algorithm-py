'''
맞았습니다!
    강호에게 원래 주려고 생각했던 돈 - (받은 등수 - 1)

'''
import sys

lst = list()
for _ in range(int(sys.stdin.readline())):
    lst.append(int(sys.stdin.readline()))

lst.sort(reverse=True)
result = 0
for i in range(len(lst)):
    value = lst[i]-i
    if lst[i]-i < 0:
        value = 0
    result += value

print(result)