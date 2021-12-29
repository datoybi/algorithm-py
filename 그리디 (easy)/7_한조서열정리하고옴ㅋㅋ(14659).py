'''
맞았습니다!

자신보다 낮은 봉우리에 서있는 적들만 처치
처음 출발한 봉우리보다 높은 봉우리를 만나면 그대로 공격을 포기

'''
import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
max_val = 0

for i in range(len(lst)):
    count = 0
    for j in range(i+1, len(lst)):
        if lst[j] < lst[i]:
            count += 1
        else:
            break
    max_val = max(max_val, count)
print(max_val)

        
