n = int(input()) 
result = []
stack = []
count = 1

for i in range(1, n+1):
    print('count : ' , count)
    data = int(input())
    print('data : ' , data)

    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else :
        print('NO')
        exit(0)

for i in result:
    print(i)