# queue -> first in first out
import sys
input = sys.stdin.readline
lst = []

def getSize():
    return len(lst)

def size():
    print(len(lst))

def push(n):
    lst.append(n)

def pop():
    if getSize() != 0:
        print(lst[0])
        del lst[0]
    else:
        print(-1)

def empty():
    if getSize() == 0:
        print(1)
    else:
        print(0)

def front():
    if getSize() == 0: 
        print(-1)
    else:
        print(lst[0])

def back():
    if getSize() == 0: 
        print(-1)
    else:
        print(lst[-1])

for _ in range(int(input())):
    tmp = input().rstrip()

    if tmp.find(' ') != -1:
        a, b = map(str, tmp.split())
        if a == 'push':
            push(b)
    else:
        if tmp == 'size':
            size()
        if tmp == 'empty':
            empty()
        if tmp == 'front':
            front()
        if tmp == 'pop':
            pop()
        if tmp == 'back':
            back()
            