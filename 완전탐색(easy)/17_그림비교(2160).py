'''
맞왜틀!!!
'''
N = int(input())
pic = list() 
minimum, ans1, ans2= 36, 0, 0

for _ in range(0,N):
    row = []
    for i in range(0,5):
        row.append(input())
    pic.append(row)

for pic1 in range(0,N):
    for pic2 in range(pic1+1,N):
        cnt = 0
        for i in range(0, 5):
            for j in range(0,7): 
                if pic[pic1][i][j] != pic[pic2][i][j]:
                    cnt += 1
        if minimum > cnt :
            minimum = cnt
            ans1 = pic1
            ans2 = pic2

print(f'{ans1+1} {ans2+1}')
