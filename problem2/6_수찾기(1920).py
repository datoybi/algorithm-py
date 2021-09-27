# 정답
# 내코드
'''
N, n_list = input(), list(map(int, input().split(' ')))
M, m_list = input(), list(map(int, input().split(' ')))

# print(n_list, m_list)

for i in m_list:
    if i in n_list:
        print('1')
    else:
        print('0')

'''
# 강사 코드
N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = input()

for i in list(map(int, input().split())):
    print(A.get(i, 0))
    # print(1 if i in A else 0)