'''
첫문제부터 어렵다 흑 

4 5
00110
00011
11111
00000

'''

n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]
lst.insert(0,)
print(lst)

visited = [False] * n