'''
정답의 최대치 
    부분 수열의 개수 상한 : 2^20 <= 1048576
        정답 변수는 int 형 변수를 쓰면 된다
    부분 수열의 합 상한: 20*1000000
        합을 기록하는 변수는 int형 변수를 쓰면 된다.

중복이 가능하고 순서가 있어야 한다.
N= 2, M = 20과 동일
따라서 시간복잡도는 2^20 = 100만

'''
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0


def rec_func(k, value):
    if k == n:
        global ans
        if value == S:
            ans += 1
    else:
        rec_func(k + 1, value + nums[k])
        rec_func(k + 1, value)


rec_func(0, 0)
if s == 0:
    ans -= 1
print(ans)
