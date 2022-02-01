# 맞았습니다!
import sys

N = int(sys.stdin.readline())
lst = [float(sys.stdin.readline()) for _ in range(N)]
dp = [0 for _ in range(N)]
dp[0] = lst[0]

for i in range(1, N):
    dp[i] = max(dp[i-1] * lst[i], lst[i])
    # dp[i] = round(dp[i], 3)
    # 이것떄문에 계속 틀렸었는데 문제를 잘 읽어야 한다. 계산된 값을 셋쨰짜리까지 반올림해야함..

print("%.3f"  %max(dp)) 



# import sys

# N = int(sys.stdin.readline())
# lst = list()
# dp = [0 for _ in range(N)]

# for i in range(N):
#     lst.append(float(sys.stdin.readline()))
# dp[0] = lst[0]

# for i in range(1, N):
#     dp[i] = max(dp[i-1] * lst[i], lst[i])
#     dp[i] = round(dp[i], 3)

# print(dp)
# # print(max(dp))    
# print("%.3f"  %max(dp)) 
