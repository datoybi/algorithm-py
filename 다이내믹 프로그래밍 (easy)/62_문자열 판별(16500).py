import itertools

s = input()
a = []
for _ in range(int(input())):
    a.append(input())

lst = []
for i in range(1, len(a)+1):
    tmp = list(map(''.join, itertools.permutations(a, i)))
    for j in tmp:
        lst.append(j) 

print(lst)

if s in lst:
    print(1)
else:
    print(0)

'''
abcefg
3
abc
efg
abce

aaaaaaaaaa
2
aaaa
aaa
'''