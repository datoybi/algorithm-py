'''
내 구현방법
시간복잡도
	O(N)
공간복잡도
	N
메모리계산
	258MB =  258,000,000 / 4 = 64500000
	100001개의 int니까 메모리 괜찮다

강사
	입출력: -2의 62제곱 ~ 2의 62제곱 이니까
	int 범위로는 감당이 안되니까 long을 쓰자!

가장 쉬운 방법 (O(N제곱))
하지만 이방법은 시간초과가 난다.
N이 최대 100000인데 *2하면 백억이기 떄문

접근
	같은 숫자를 빨리 보는 방법 O(N log N)

'''

import sys
input = sys.stdin.readline
N = int(input())
lst = [int(input()) for _ in range(N)]
# mode: 최빈값, modeCnt: 최빈값의 등장 횟수, curCnt: 현재값(a[1])의 등장 횟수
mode = lst[0]
modeCnt = 1
curCnt = 1
lst.sort()
print(lst)

for i in range(1, N):
    print(lst[i])
    print(curCnt, modeCnt, mode)
    if modeCnt < curCnt:
        modeCnt = curCnt
        mode = lst[i]
    if lst[i] == lst[i-1]:
        curCnt += 1
        modeCnt += 1
    else:
    curCnt = 1

print(curCnt, modeCnt, mode)
