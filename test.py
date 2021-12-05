for _ in range(int(input())):
    N = input()
    result = 0
    while N != '6174':
        li = sorted(list(map(str, N)))
        A, B = int(''.join(li)), int(''.join(li[::-1]))
        N = str(B - A).zfill(4)
        result += 1
    print(result)