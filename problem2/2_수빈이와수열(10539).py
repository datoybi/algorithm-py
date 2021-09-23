# 정답 맞춤 
# 내 코드
'''
N, lst, n_lst = input(), list(map(int, input().split())), list()

for i in range(len(lst)):
    n_lst.append(lst[i]*(i+1)-sum(n_lst))
    
for i in n_lst:
    print(i, end=' ')

'''

# 강사 코드
N, B = int(input()), list(map(int, input().split()))
A = [B[0]]

for i in range(1, N):
    A.append(B[i] * (i+1) - sum(A))


for i in A: 
    print(i, end=' ')

