# from functools import*
# w=cache(lambda a,b,c:1>min(a,b,c)or(max(a,b,c)>20)<<20or-(a<b<c)&w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)or w(a:=a-1,b,c)+w(a,b-1,c)+w(a,b,c-1)-w(a,b-1,c-1))
# *U,t=open(0)
# for t in U:a,b,c=t=*map(int,t.split()),;print(f'w{t} =',+w(*t))

l = int(input())
m = int(input())

print(m-l+m)