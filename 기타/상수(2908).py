n, m = map(str, input().split())

print(n[::-1] if int(n[::-1]) > int(m[::-1]) else m[::-1])