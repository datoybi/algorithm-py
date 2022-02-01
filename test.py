# 나중에 또 풀어보기
n = int(input())
day = []
cost = []
dp=[]

for i in range(n):
  x,y = map(int, input().split())
  day.append(x)
  cost.append(y)
  dp.append(y)
dp.append(0)  #뒤에 0을 추가해서 인덱스초과 오류 방지

print(day)
print(cost)
print(dp)

#뒤에서부터 확인 - 왜 이렇게 되는지는 모르겟다
for i in range(n-1, -1, -1):
    print(i)
    if day[i] + i > n: # 데드라인이 기한을 넘어가는경우
        dp[i] = dp[i+1]
    else:
        print(dp[i+1], cost[i] + dp[i + day[i]])
        dp[i] = max(dp[i+1], cost[i] + dp[i + day[i]])

print(dp[0])