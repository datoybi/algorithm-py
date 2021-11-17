'''
맞았습니다!
 (일단 포문 세개 돌리면서) 각각의 숫자에 대해 모든 경우의 수 에서 곱셉이 가장 큰 경우 추출
 삼중 포문을 대체할 수 있는 대체재가 뭐가 있을까... 

 힌트 -> for문을 돌리는것 보다 정렬을 해서 경우의 수를 판별하기
 왜 정렬할 생각을 못했을까ㅜ

6
5 10 -2 3 5 2

6
-3 -2 0 1 1 7
42
'''
import sys

# 입력
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

# 정렬
lst.sort()
r_lst = list(reversed(lst)) # 내림차순 정렬
# print(r_lst)

print(
  max(r_lst[0]*r_lst[1]*r_lst[2], # 세개의 수 중 세개의 수가 양수일 경우
  r_lst[0]*r_lst[1],              # 두개의 수가 양수일 경우
  r_lst[-1]*r_lst[-2],            # 두개의 수가 음수일 경우
  r_lst[-1]*r_lst[-2]*r_lst[0],   # 세개의 수 중 두개의 수가 음수고 하나의 수가 양수일 경우
  )
)












# 시간초과 .. 삼중포문 노우 
# import sys

# N = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# max_val = 0

# for i in range(len(lst)):
#   for j in range(i+1, len(lst)):
#     for z in range(j+1, len(lst)):
#         #print(i, j, z)
#         max_val = max(max_val, lst[i]*lst[j]*lst[z], lst[i]*lst[j], lst[i]*lst[z])
#     #   print(i, j, z, lst[i]*lst[j]*lst[z], lst[i]*lst[j])

# print(max_val)

