'''
    같은 구성 : 같은 문자가 같은 개수만큼 있는 것

    비슷한 단어 : 한 단어에서 한문자를 더하거나 빼거나
    하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게되는

    같은 구성 -> 비슷한 단어임

4
ABC
ABCD
BC
PCD

2

2
A
B

1
'''
import copy

tc = int(input())
word = input()
test_lst = list()
zero_lst = [0 for i in range(130)]
count = 0

for _ in range(tc-1):
    test_lst.append(input())

for i in range(len(word)): # word setting 
    zero_lst[ord(word[i])] += 1
    
for j in range(len(test_lst)):
    tmp_lst = copy.deepcopy(zero_lst)
    for z in range(len(test_lst[j])):
       print(test_lst[j][z])
       tmp_lst[ord(test_lst[j][z])] -= 1
    print(tmp_lst)
    print(max(tmp_lst), min(tmp_lst), abs(max(tmp_lst)) + abs(min(tmp_lst)))

    value = 0
    for k in tmp_lst:
        if k != 0:
            value += 1
    value = max(tmp_lst) + min(tmp_lst)
    
    print(value)
    if value < 2:
        count += 1

print(count)
