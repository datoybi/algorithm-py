N = int(input())
num = 1
result = 0

while N:
    if N < num:
        num = 1
    else:        
        N = N-num
        print(num , N)
        num += 1
        result += 1

print(result)