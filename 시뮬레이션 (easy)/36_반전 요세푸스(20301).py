# 3 6 2 7 5 1 4
import sys

N, K, M = list(map(int, sys.stdin.readline().split()))
lst = [i for i in range(1,N+1)]
result = list()
print(lst)
# print(lst) [1, 2, 3, 4, 5, 6, 7]
idx = 0
count = 0
for _ in range(10):
    print('idx : ' , idx, ' K : ', K, 'len(lst) : ', len(lst))
    # n보다 k가 작으니까 여러번 도는 경우의 수는 카운트 안해도됨
    idx = (idx + K) % len(lst)-1
    print('idx : ' , idx, 'lst[idx] : ' , lst[idx])
    result.append(lst[idx])
    del lst[idx]
    print('result : ' , result)
    print('lst : ' , lst)
    