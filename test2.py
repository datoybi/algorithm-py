from sys import stdin 
input = stdin.readline 

def dfs(n, val): 
    global res 
    if n >= N and res < val: 
        res = val 
        return 

    for i in range(n, N): 
        dfs(i+2, val+arr[i][2]) 

N = int(input()) 
arr = [tuple(map(int, input().split())) for i in range(N)] 
arr.sort() 
res = 0 
dfs(0, 0) 
print(res)
