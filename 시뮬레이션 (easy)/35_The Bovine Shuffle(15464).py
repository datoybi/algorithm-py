'''
맞았습니다!

영어라 쫄았는데 그렇게 어려운 문제가 아니였다.

5
1 3 4 5 2
1234567 2222222 3333333 4444444 5555555
1234567 3333333 4444444 5555555 2222222
1234567 4444444 5555555 2222222 3333333
1234567 5555555 2222222 3333333 4444444

소 N 1~100
셔플을 수행한 다음 다른 순서로 줄을 선다.

젖소에게 고유한 7자리 id가 할당
3번의 셔플후 소의 순서를 알게되면 초기 순서를 알아맞추기

N 소의 수
a1~aN까지의 정수
3번의 셔플 이후의 소들의 id

'''
import sys, copy

N = int(sys.stdin.readline())
order = list(map(int, sys.stdin.readline().split()))
id = list(map(str, sys.stdin.readline().split()))
lst = [0 for _ in range(N)]
# print(N, order, id)

for _ in range(3):
    for i in range(N):
        lst[i] = id[order[i]-1]
    id = copy.deepcopy(lst)

for i in lst:
    print(i)