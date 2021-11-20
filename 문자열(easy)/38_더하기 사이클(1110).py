
import sys

N = sys.stdin.readline().rstrip()
original, count = N, 0

if int(N) < 10: # 10보다 작을 때 앞에 0 붙여주기
    N = '0'+ N

# print(N)
while True:
    new = int(N[0]) + int(N[1])
    N = N[1] + str(new)[-1]
    count += 1

    if int(original) == int(N):
        print(count)
        exit(0)
