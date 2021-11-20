# 맞았습니다!
import sys

N = int(sys.stdin.readline())
original, new = list(sys.stdin.readline().rstrip()), list(sys.stdin.readline().rstrip())

for _ in range(N):
    for i in range(len(original)):
        if original[i] == '0':
            original[i] =  '1'
        else:
            original[i] = '0'

print("Deletion succeeded" if original == new else "Deletion failed")
