n = int(input())
lst = list(map(int, input().split()))
cnt = 0

for i in range(n):
    flag = False
    for j in range(2, lst[i]):
        if lst[i] % j == 0:
            flag = True
            break
    if lst[i] != 1 and flag == False:
        cnt += 1

print(cnt)