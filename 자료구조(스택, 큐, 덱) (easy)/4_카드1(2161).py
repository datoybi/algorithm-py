'''
1번 카드가 젤 위에 N번이 젤 아래에
제일 위에 카드를 제일 아래에 있는 카드로 옮기기

'''
import sys

lst = [i+1 for i in range(int(sys.stdin.readline()))]
result = list()

for i in range(len(lst)):
    if len(lst) == 1:
        break
    result.append(lst[0])
    del lst[0]
    if len(lst) == 1:
        break
    lst.append(lst[0])
    del lst[0]
    

for i in result:
    print(i, end = ' ')
print(lst[0])
