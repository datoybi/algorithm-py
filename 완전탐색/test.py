def check(one, two, three, s, b):
    for i in range(100,1000):
        ns, nb = 0, 0
        if(res[i]):
            n_one = int(i/100)
            n_two = int((i%100)/10)
            n_three = int((i%100)%10)
            
            if(one == n_one):
                ns += 1
            if(two == n_two):
                ns += 1
            if(three == n_three):
                ns += 1
            
            if(one != n_one and (one == n_two or one == n_three)):
                nb += 1
            if(two != n_two and (two == n_one or two == n_three)):
                nb += 1
            if(three != n_three and (three == n_one or three == n_two)):
                nb += 1
            
            if(ns != s or nb != b):
                res[i] = False

N = int(input())
res = [True for i in range(1000)]

for i in range(100,1000):
    one = int(i/100)
    two = int((i%100)/10)
    three = int((i%100)%10)
    if(one == two or two == three or three == one):
        res[i] = False
    if(one == 0 or two == 0 or three == 0):
        res[i] = False

for n in range(N):
    num, s, b = map(int, input().split())        
    num = str(num)
    one, two, three = int(num[0]),int(num[1]),int(num[2])
    check(one, two, three, s, b)

cnt = 0
for i in range(100,1000):
    if(res[i]):
        cnt += 1

print(cnt)