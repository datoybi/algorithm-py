'''
맞았습니다! 
O(n)

3개 중 가장 싼 1개 무료
최소비용

'''
import sys

lst = list()
for _ in range(int(sys.stdin.readline())):
    lst.append(int(sys.stdin.readline()))
lst.sort(reverse=True)
value = 0

for i in range(1, len(lst)//3+1):
    value += sum(lst[(i-1)*3:i*3]) - min(lst[(i-1)*3:i*3])
    if i == len(lst) // 3:
       value += sum(lst[i*3:])

print(value)

    
    