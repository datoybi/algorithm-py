# 맞았습니다! 
# :-) :-(

import sys

sentence, sad, happy = sys.stdin.readline().rstrip(), 0, 0

for i in range(len(sentence)):
    # print(sentence[i:i+3])
    if sentence[i:i+3] == ':-)':
        happy += 1
    elif sentence[i:i+3] == ':-(':
        sad += 1

# 판별
if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif sad > happy:
    print('sad')
else:
    print('unsure')