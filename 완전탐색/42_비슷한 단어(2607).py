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
모든 경우의 수에 대해 처리를 해주었다.. 다른 사람들 코드를 보니까 보통 딕셔너리나 list를 사용하여 나랑 비슷하게 풀었다.

'''
import copy

tc = int(input())
word = input()
test_lst = list()
zero_lst = [0 for _ in range(130)] # list를 0으로 세팅
count = 0 

for _ in range(tc-1):
    test_lst.append(input())

for i in range(len(word)): # word setting
    zero_lst[ord(word[i])] += 1
    
for j in range(len(test_lst)):
    tmp_lst = copy.deepcopy(zero_lst) # 0으로 세팅한 리스트 copy
    for z in range(len(test_lst[j])): # 갯수만큼 해당 아스키코드의 원소에 -1 더하기
       tmp_lst[ord(test_lst[j][z])] -= 1
    
    value = 0
    for k in tmp_lst:
        if k != 0:
            value += 1
    # print(test_lst[j], max(tmp_lst) , min(tmp_lst), + (abs(max(tmp_lst)) + abs(min(tmp_lst))) ,  value)

    # 0의 min 개수와 max 개수가 2가 안넘어야하고, abs(max(tmp_lst)) + abs(min(tmp_lst))가 2를 넘지 않아야 하는 이유는 한단어가 교환될 수 있으니까(min도 1이고 max도 1이라는 거니까 그둘이 교환하면 0이 된다.)
    # 또한 value는 0이 아닌 갯수인데, 그것이 2가 넘지 않아야 하고(위랑 같은 이유), 그리고 abs(len(word) - len(test_lst[j]))가 1을 넘지 않아야 하는 이유는 word가 1고 abc 인경우 판별하기 위함이다
    if abs(max(tmp_lst)) <= 1 and abs(min(tmp_lst)) <= 1 and abs(max(tmp_lst)) + abs(min(tmp_lst)) <= 2 and value <=2 and abs(len(word) - len(test_lst[j])) <= 1: 
        # print(test_lst[j], max(tmp_lst) , abs(max(tmp_lst)) + abs(min(tmp_lst)),  min(tmp_lst), value)
        count += 1

print(count)

