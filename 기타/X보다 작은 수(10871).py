n, x = map(int, input().split())
print(n, x)
lst = list(map(int, input().split()))

for i in lst:
    if x > i:
        print(i, end=' ')