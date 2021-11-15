import sys

T = int(sys.stdin.readline())

for _ in range(T):
    #팀의 개수, 문제의 개수, ID, 로그 엔트리 개수
    n, k, t, m = map(int, sys.stdin.readline().split())
    #arr[i] = [ID, score1, ..., scorek,최종점수, 제출횟수, 제출시간]
    arr = [[0]*(k+4) for _ in range(n)] 
    # [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

    #팀 ID
    for i in range(n):
        arr[i][0] = i+1
    
    print(arr)
    # [[1, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0]]

    for time in range(m):
        #ID, 문제 번호, 획득 점수
        i, j, s = map(int, sys.stdin.readline().split())
        arr[i-1][j] = max(arr[i-1][j], s) #문제별 최고점수
        arr[i-1][k+2]+=1 #제출횟수
        arr[i-1][k+3] = time #마지막 제출 시간

    print(arr)
    # [[1, 30, 40, 0, 0, 0, 3, 3], [2, 0, 0, 30, 0, 0, 1, 1], [3, 70, 0, 0, 0, 0, 1, 4]]

    for i in range(n):
        for j in range(1,k+1):
            arr[i][k+1] += arr[i][j] #최종점수 계산
    
    #정렬
    ans = sorted(arr, key = lambda x: (-x[k+1], x[k+2], x[k+3]))
    
    #내 팀 찾기
    for i in range(n):
        if (ans[i][0]==t):
            print(i+1)
            break