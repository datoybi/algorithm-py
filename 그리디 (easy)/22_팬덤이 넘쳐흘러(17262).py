''''
하다가 규칙찾기가 번거로워서 소스코드를 참고했다.
왜 이런식으로 풀었는지는 잘 모르겠는데 
첫번째 원소로 정렬한 뒤 맨 마지막의 첫번째 원소 - 두번째 원소로 정렬한 뒤 첫번째 순서의 두번째원소
하면 답이 나온답.

아 그리고 

'''
n=int(input())

left=[]
right=[]

for i in range(n):
    x,y=map(int,input().split())
    left.append(x)
    right.append(y)

L=min(right)
R=max(left)

result=R-L if R-L>0 else 0
print(result)



# import sys
# fans = []
# for _ in range(int(sys.stdin.readline())):
#     fans.append(list(map(int, sys.stdin.readline().split())))

# a = sorted(fans, key=lambda x: x[0])
# b = sorted(fans, key=lambda x: x[1])

# result = a[-1][0] - b[0][1]

# if result <= 0:
#     print(0)
# else:
#     print(result)


# import sys
# minval = 100000
# maxval = 0
# count = 0
# val = 0
# cnt = 0
# whole = set()

# for _ in range(int(sys.stdin.readline())):
#     N, M = list(map(int, sys.stdin.readline().split()))
#     check = False
#     for i in range(N, M+1): # whole 안에 있으면
#         if i in whole:
#             check = True
#             val = min(maxval, M)

#         minval = max(minval, N)
#         maxval = min(maxval, M)

#     if check == False and len(whole) == 0: # 맨처음
#         minval = N; maxval = M; val = M

#     elif check == False and len(whole) != 0: # 없으면
#         count += N - maxval
#         cnt += minval - val
#         minval = N; maxval = M

#     for i in range(N, M+1):
#         whole.add(i)

#     print('minval : ' , minval , ' , ' , 'maxval : ' , maxval, ', val : ' , val)
#     print('count : ' , count)
#     print('cnt : ' , cnt)

# print(count)
# print(whole)
# print('cnt : ' , cnt)