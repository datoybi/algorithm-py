import itertools

lst = ['1', '2', '3']

print(list(itertools.permutations(lst, 2)))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
for i in itertools.permutations(lst, 2):
    print(i)
    # ('1', '2')
    # ('1', '3')
    # ('2', '1')
    # ('2', '3')
    # ('3', '1')
    # ('3', '2')

    print(''.join(i))
    # 12
    # 13
    # 21
    # 23
    # 31
    # 32