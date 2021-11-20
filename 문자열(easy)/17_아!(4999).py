# 맞았습니다!

import sys

mine, doctor = sys.stdin.readline().strip(), sys.stdin.readline().strip()

if len(mine)-1 >= len(doctor)-1:
    print('go')
else:
    print('no')
