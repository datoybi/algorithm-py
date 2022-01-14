numbers = [0]*500001
N = int(input())
arr = map(int,input().split())
for k in arr:
    numbers[k] += 1
print(max(numbers))


























