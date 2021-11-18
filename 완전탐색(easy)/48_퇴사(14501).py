'''
담에 꼭 풀어보기 ㅠ

봐도 로직을 어캐 짜야 할지 모르겠다ㅜ 
앞에서부터 순차적으로 하는건 가능한데 
두번째 예의 경우 2 20을 건너뛰고 3 30을 택해야 하는걸 어떻게 구현해야 할까?


7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

45

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50

90
'''
# 남 코드 dp를 사용했는데 나도 좀 그쪽으로 많이 봐야겠다ㅠ담에 꼭 풀어보기

n = int(input())
t = []
p = []
dp = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0) # 마지막에 0 append는 왜?!?!?!?!??

# print(t) # [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
# print(p) # [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
# print(dp) # [50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 0]

for i in range(n - 1, -1, -1): # 9 ~ 0 더 크면 0이된다. 시간이 크면 부적합하니까
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        # print(i , dp[i], dp[i + 1],  p[i] ,t[i],  dp[i + t[i]] )
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]]) # 왜 이렇게 하는 건지 노이해다..
    
    # print('dp :', dp)
print(dp[0])


# 왜 거꾸로 할까?




















# 내 코드  - 못품
import sys
N = int(sys.stdin.readline())
lst = list()

for _ in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

print(lst) 
# [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
cnt = lst[0][0]

for i in range(N):
    max_val = 0
    j = 0
    while True:
        print(cnt, lst[j], max_val)
        cnt = lst[j][0] # 5 1 2
        j += cnt # 5 6 8
        if j > len(lst):
            break
        max_val += lst[j][1] # 50 10 20

        print(cnt, lst[j], max_val)

        











    # for j in range(len(lst)):
    #     print(cnt, lst[j])
    #     max_val += lst[j][1]
    #     j = cnt-1
    #     cnt = lst[j][0]
    #     print(cnt, max_val)
        

    
