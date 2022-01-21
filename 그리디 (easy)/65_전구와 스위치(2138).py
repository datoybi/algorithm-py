'''
고민을 참 많이 했는데 자꾸 틀렸다고 한다.. 다 음 에 풀 어 보 자

- 전구 스위치에 상태를 확인할 함수와 전구의 상태를 바꿔줄 함수를 만든다.
- 첫 번째 전구의 스위치는 첫 번째 전구와 이후에 전구의 상태만을 바꾸므로 다음 2가지 경우로 나눈다.(아거 이해를 못하겟담ㅎㅎ)
- 첫 번째 전구를 켰는지와 안 켰는지를 나누어 문제를 수행한다.
- 이후부터는 이전 전구를 확인하면서 전구의 상태를 바꿔준다.
- 이후 전구는 마지막 전구가 아니라면 바꿔준다.
- 현재 전구와 바꿔야 하는 전구가 똑같으면 멈춰주고 카운트를 리턴한다.
- 그렇지 않다면 현재 전구를 바꿔야 하는 전구로 바꾸지 못하는 것을 의미하며 -1을 출력한다.


'''





import sys

N = int(sys.stdin.readline())
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

for i in range(N):
    print(a)
    if i-1 >= 0:
        a[i-1] = str(1 - int(a[i-1]))
    if a[i] == '0':
        a[i] = str(1 - int(a[i]))
    if i+1 <= N-1:
        a[i+1] = str(1 - int(a[i+1]))
    if a == b:
        print(i+1)
        exit(0)

print(-1)

# 뭔가 그리디 하게 풀려고 했는데 안된다! 구냥 완탐으로 돌려봐야겠다..
# import sys

# N = int(sys.stdin.readline())
# a = list(sys.stdin.readline().rstrip())
# b = list(sys.stdin.readline().rstrip())
# check = ['1' for _ in range(N)]
# check[0] = '0'
# check[-1] = '0'
# print(check)

# for i in range(N):
#     if a[i] != '0':
#         if check[i] == '0':
#             check[i] = '1'
#         else:
#             check[i] = '0'

# print(check)
# flag = False
# if check == b:
#     print(N)
# else:
#     for i in range(N):
#         if check[i] != b[i]:
#             if i == 0:
#                 print(-1)
#             else:
#                 print(i+1)
#             break  
        
 
