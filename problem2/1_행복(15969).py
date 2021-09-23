'''
# 정답 맞춤 
# 내 코드

n = int(input())

# for i in range(n): # 0~4
lst = list(map(int, input().split(' ')))
lst.sort()
min = lst[0]
max = lst[-1]
print(max-min)


'''

N, lst = input(), list(map(int, input().split()))

print(max(lst)-min(lst))