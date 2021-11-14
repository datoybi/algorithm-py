import copy

tc = int(input())
word = input()
test_lst = list()
zero_lst = [0 for i in range(130)] # list를 0으로 세팅
count = 0 

for _ in range(tc-1):
    test_lst.append(input())

for i in range(len(word)): # word setting
    zero_lst[ord(word[i])] += 1
    
for j in range(len(test_lst)):
    tmp_lst = copy.deepcopy(zero_lst) # 0으로 세팅한 리스트 copy
    for z in range(len(test_lst[j])):
       tmp_lst[ord(test_lst[j][z])] -= 1

    value = 0
    for k in tmp_lst:
        if k != 0:
            value += 1

    if abs(max(tmp_lst)) <= 1 and abs(min(tmp_lst)) <= 1 and abs(max(tmp_lst)) + abs(min(tmp_lst)) <= 2 and value <=2 and abs(len(word) - len(test_lst[j])) <= 1: 
        count += 1
    
print(count)

