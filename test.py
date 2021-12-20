
n=int(input())
t=int(input())
a=[1]*n
for i in range(t):
    s,f=map(int,input().split())
    for j in range(s,f):
        a[j]=0
    print(a)
print(a.count(1))