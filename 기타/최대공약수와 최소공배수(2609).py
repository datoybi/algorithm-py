n, m = map(int, input().split())
value, gcd, lcm = max(n, m), 1, 1

for i in range(value, 1, -1):
    # print(i)
    if n % i == 0 and m % i == 0:
        gcd = i
        break

print(gcd)
print(n * m // gcd)
