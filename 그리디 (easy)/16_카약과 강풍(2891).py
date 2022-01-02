'''
맞았습니다!
자신의 바로 다음이나 전에 경기하는 팀에게만 빌려줄 수 있음
출발하지 못한 팀의 최소값

팀의 수 N(2 <= N <= 10), 
카약이 손상된 팀의 수 S(1 <= S <= N), 
카약을 더 가져온 팀의 수 R(1 <= S <= N)
카약이 손상된 팀의 번호
카약을 더 가져온 팀의 번호 

'''
# 왜 이건 안되냐고오오오오오
import sys

N, S, R = list(map(int, sys.stdin.readline().split()))
S_lst = list(map(int, sys.stdin.readline().split()))
R_lst = list(map(int, sys.stdin.readline().split()))
cnt = S

for i in range(len(S_lst)):
    for j in range(len(R_lst)):
        if S_lst[i] in R_lst:
            cnt -= 1
            print('삭제할 R_lst[j]1 : ', R_lst[R_lst.index(S_lst[i])])
            del R_lst[R_lst.index(S_lst[i])]
            break
        elif R_lst[j] == S_lst[i] + 1 or R_lst[j] == S_lst[i] - 1:
            cnt -= 1
            print('삭제할 R_lst[j]2 : ', R_lst[j])
            del R_lst[j]
            break

print(cnt)


# 이건 됨 
N,S,R = map(int, input().split())
broken = list(map(int, input().split()))
extra = list(map(int, input().split()))
cnt = S

for i in extra:
  if i in broken:
    broken.remove(i)
    extra.remove(i)
    cnt -= 1

for i in broken:
  for j in extra:
    if j-1 <= i <= j+1:
      extra.remove(j)
      cnt -= 1
      break
    elif j+1 < i:
      break
    
print(cnt)