n = int(input())
lst = list(map(int, input().split()))
max_val = max(lst)
for i in range(len(lst)):
    lst[i] = lst[i] / max_val*100

print(lst)
print(sum(lst)/n)
