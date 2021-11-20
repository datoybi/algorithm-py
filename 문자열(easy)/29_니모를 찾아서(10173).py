# 맞았습니다!
import sys

while True:
    sentence = list(sys.stdin.readline().split())

    if sentence[0] == 'EOI': break
    answer = False
    for i in sentence:
        if 'nemo' in i.lower():
            answer = True
            break

    print('Found' if answer == True else 'Missing')