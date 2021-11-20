# 맞았습니다!
import sys

for _ in range(int(sys.stdin.readline())):
    num1, num2 = sys.stdin.readline().strip(), sys.stdin.readline().strip()
    distance = 0

    for i in range(len(num1)):
        if num1[i] != num2[i]:
            distance += 1

    print(f'Hamming distance is {distance}.')