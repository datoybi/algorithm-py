'''
시간복잡도
    N개 중 중복을 허용해서 M개를 고르기
    아 1 2는 있는데 2 1은 없네 
    또 시간복잡도 못찾겠다ㅠ 
    아.. 보니까 N^M 보단 작다 이렇게 표현한다. 
    왜냐면 이걸 표현하기에는 수학적인 지식이 많이 필요하다고 한다.
    시간복잡도는 대략적으로 구해도 되는 거니까 그렇게 구하자.
    8^8 보단 작다 ! 8^8 = 대략 천육백만인데 1억보다 작으니 ㄱㅊ함!

공간복잡도 O(M)

'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
selected = [0 for _ in range(M)]

def solution(k):
    if k == M:
        for x in selected:
            print(x, end= ' ')
        print()
    else:
        for i in range(1, N+1):
            if i >= max(selected):
                selected[k] = i 
                solution(k + 1)
                selected[k] = 0

solution(0)

'''
import sys
n, m = map(int, sys.stdin.readline().split(' '))

selected = [0 for _ in range(m)]
used = [0 for _ in range(n + 1)]
def rec_func(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    else:
        start = 1 if k == 0 else selected[k - 1]
        for cand in range(start, n + 1):
            selected[k] = cand
            rec_func(k + 1)
            selected[k] = 0

rec_func(0)

'''