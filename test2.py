for _ in range(int(input())):
    n, s = map(str, input().split())
    for i in range(len(s)):
        print(s[i] * int(n), end = '')
    print()