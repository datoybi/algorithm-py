
import sys

num1, num2 = map(str, sys.stdin.readline().split())
sum = str(int(num1[::-1]) + int(num2[::-1]))
print(int(sum[::-1]))
