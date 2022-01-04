'''
3
2 4
1 5
6 7

ans 2

4
2 4
1 5
6 7
8 9

4


'''
n=int(input())

left=[]
right=[]

for i in range(n):
    x,y=map(int,input().split())
    left.append(x)
    right.append(y)


L=min(right)
R=max(left)

print(L, R)

result=R-L if R-L>0 else 0
print(result)



