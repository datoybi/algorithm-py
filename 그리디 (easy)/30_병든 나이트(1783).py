'''
흠 어캐 접근해야할지 모르겟음 분기점이 뭔지도 모르겠고,,
담에 또 풀어보긩긩
https://lipcoder.tistory.com/94
병든 나이트가 도달할 수 있는 칸의 개수를 세는 것이 아니고, 
출발점으로부터 출발해서 막다른 곳에 도달하기까지의 
이동 횟수가 가장 많은 것을 찾는 문제입니다.

'''

M, N = list(map(int, input().split())) # 세로 N, 가로 M
answer = 0

if N == 1:
    answer = 1
elif N == 2:
    answer = min(4, (M + 1) // 2)
elif M < 7:
    answer = min(4, M)
else:
    answer = M - 7 + 5

print(answer)