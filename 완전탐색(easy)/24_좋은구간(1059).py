'''
    맞았습니다!
    -----
    아오 왜자꾸 틀리는지 모르겠다 
    반례 다 적용해봐도 안된다..
    왜 틀리는지 잘 모르겠따 머리아프당.. 
    --- 
    이랬었는데 결국 반례 찾아서 맞았다
    반례

    2

    3 7

    2

    요 반례를 적용하니 되었다..

'''
L = int(input())
S = list(map(int, input().split()))
S.sort()
n = int(input())

max_num, min_num, count = 1000, 0, 0

for i in range(0, L): 
    if n in S: # 집합 안에 n이 있는 경우 
        print(0) 
        exit(0)
    if n <= S[i]: 
        if i == 0: # S[0]이 n보다 큰 경우 -> 그걸 max_num으로
            max_num = S[i]
        else: # 그렇지 않은 경우 (중간인 경우)
            max_num = S[i] 
            min_num = S[i-1]
        break

if L == 1: # 만약 집합의 원소가 1개인 경우
    max_num = S[i]
# print(min_num, max_num)

for i in range(min_num+1, n+1):
    # print(i)
    for j in range(i+1, max_num):
        if n <= j :
            # print(i, j)
            count+=1
        
print(count)


# 수학적 접근
# import sys
# input=sys.stdin.readline

# l=int(input())
# a=list(map(int,input().split()))
# a=[0]+a
# a.sort()
# n=int(input())

# left=0
# right=0
# if n in a:
#     print(0)
#     sys.exit()

# for x in a:
#     if n>x:
#         left=x+1
#     else:
#         right=x-1
#         break
# print(left,right)
# print(right-left+(right-n)*(n-left)) # 이 식을 어캐 생각해낸거지..?

