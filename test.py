'''
1-10+2-5-2

-9
-11
-16
-18
'''
a = input().split('-')
b = [sum(map(int, i.split('+'))) for i in a]
print(a)
print(b)
print(b[0] * 2 - sum(b))