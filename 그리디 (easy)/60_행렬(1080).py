'''
맞았습니다!

어캐 접근해야 할지 모르겠었는데 밑에 블로그 보고 대충 감을 잡았다. 
대충 요약하자면,
1. 바꿔야 되는지 안바꿔도 되는지를 판별(check list)
2. 바꿔야되는것만 3x3 크기 반전시키기
3. 예외처리 해주기(반전되고 나서도 바꿔야되는게 있으면(T) -1 )
https://mizzo-dev.tistory.com/entry/baekjoon1080

이렇게 하면 5 × 5 행렬의 경우, 좌상단부터 
3 × 3 부분에 있는 칸만 확정해도 이 행렬을 B로 변환 가능한지 아닌지를 알 수 있습니다.

'''
import sys

N, M = list(map(int, sys.stdin.readline().split()))
lst, answer, check = list(), list(), list()
for _ in range(N):
    lst.append(list(map( str, sys.stdin.readline().rstrip())))
for _ in range(N):
    answer.append(list(map( str, sys.stdin.readline().rstrip())))
check = lst

for i in range(N):
    for j in range(M):
        if lst[i][j] == answer[i][j]:
            check[i][j] = 'F'
        else:
            check[i][j] = 'T' # T: 값이 변해야 하는 곳 (서로 다른 수니까)

cnt = 0
for i in range(0, N-2):
    for j in range(0, M-2):
        if check[i][j] == 'T':
            cnt += 1
            for l in range(i, i+3):
                for k in range(j, j+3):
                    if check[l][k] == 'T':
                        check[l][k] = 'F'
                    else:
                        check[l][k] = 'T'

for i in range(len(check)):   
    if 'T' in check[i]:
        print(-1)
        exit(0)

print(cnt)
