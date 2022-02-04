from functools import cache

@cache
def w(a, b, c):
    if (a<=0 or b<=0 or c<= 0): return 1
    if (20<a or 20<b or 20<c): return w(20, 20, 20)
    if (a<b and b<c): return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

while(1):
    a, b, c = map(int, input().split())
    if a==-1and b==-1 and c==-1: break;
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')