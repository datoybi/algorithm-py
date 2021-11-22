
import sys

count = 0
num = list('1234567')

print(num)

while True:
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])

    print(sum)

    # print(len(str(sum)))

    if len(str(sum)) != 1:
        num = str(sum)
        count += 1
    else:
        print(count)
        exit(0)

    print(num, count)
    