'''
1번 카드가 제일 위에, N번이 젤 아래에

제일 위에(1) 있는 카드를 바닥에 버린다
그다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

4

1
2
3
4

1 버림
2
3
4

2를 아래로 옮김
3
4
2

3버림 
4
2

4를 아래로 옮김
2
4

2 버림 
남은 카드 4

[1, 2, 3, 4]
'''
from collections import deque

n = int(input())
queue = deque([i for i in range(1, n+1)])
print(queue)    

for i in range(n-1):
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)
    print(queue)

print(queue[0])