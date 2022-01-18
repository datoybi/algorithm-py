'''
맞았습니다!
1. 임의의 서로 다른 두 에너지 드링크를 고른다.
2. 한쪽 에너지 드링크를 다른 쪽 에너지 드링크에 모두 붓는다. 
단, 페인은 야근 후유증으로 인해 손이 떨려, 붓는 과정에서 원래 양의 절반을 바닥에 흘리게 된다.
3. 다 붓고 남은 빈 에너지 드링크는 버린다.
1~3 과정을 에너지 드링크가 하나만 남을 때까지 반복한다.
'''

import sys

int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
value = (sum(lst)-max(lst))/2 + max(lst)

if value.is_integer()  == True:
    print(int(value))
else:
    print(value)
