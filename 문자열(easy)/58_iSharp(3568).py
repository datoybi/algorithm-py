
import sys

variable = list(map(str, sys.stdin.readline().split()))
front, lst = variable[0], list()

for i in range(1, len(variable)):
    lst.append(variable[i][0:len(variable[i])-1]) # 예쁘게 걸러서 리스트에 다시 담기

print(lst)
check = ['&', '[]', '*']

result = list()

for i in range(len(lst)):
    for j in range(len(lst)):
        print(i, j)
        if j == 0:
            result.insert(0, lst[i][j])
            result.insert(0, ' ')
        if result[i][j] != '[':
            result.insert(0, lst[i][j])
        elif result[i][j] == '[':
            result.insert(0, '[]')
        elif result[i][j] == ']':
            continue

    print(result)
    


'''
Double[][] Array[];
int&*& a&, b&*, c*&&;
ans
int&*&& a;
int&*&*& b;
int&*&&&* c;

int&*&& a;
int&*&&* b;
int&*&&&* c;

# import sys

# lst = list(sys.stdin.readline().split())

# for i in range(1, len(lst)):
#     lst[i] = lst[i].replace(',','').replace(';','')
#     tmp = list(lst[i])
#     result = lst[0]
#     j = 0

#     while True:
        
#         if tmp[-1] =='&' or tmp[-1] == '*':
#             result += tmp.pop()
#         elif tmp[-1] ==']':
#             result += tmp.pop()
#             result += tmp.pop()
#         if '&' not in tmp or '*' not in tmp or '[]' not in tmp:
#             break
#     print(result)



    #     if j >= len(tmp):
    #         break
    #     if '&' == tmp[j]:
    #         # result += '&'
    #         dic['1'] += 1
    #         tmp.remove('&')
    #     elif '[' == tmp[j]:
    #         # result += '[]'
    #         dic['2'] += 1
    #         tmp.remove('[')
    #         tmp.remove(']')
    #     elif '*' == tmp[j]:
    #         # result += '*'
    #         dic['3'] += 1
    #         tmp.remove('*')
    #     else:
    #         j += 1
            
    # for i in range()
    # print(dic)
    # v = ''.join(tmp)
    # print(f'{result} {v};')

# n = int(input())
# score = []
# for i in range(n):
#     score.append(int(input()))

# count = 0
# for i in range(n-2, -1, -1):
#     if score[i] >= score[i+1]:
#         count += score[i] - score[i+1] + 1
#         score[i] = score[i+1]-1

# print(count)
'''
  

    # if cnt != 0: # 변수길이
    #     print(f'{front}{tmp} {lst[i][0:cnt]};')
    # else:
    #     print(f'{front}{tmp} {lst[i][0]};')
























# import sys

# variable = list(map(str, sys.stdin.readline().split()))
# front, lst = variable[0], list()

# for i in range(1, len(variable)):
#     lst.append(variable[i][0:len(variable[i])-1]) # 예쁘게 걸러서 리스트에 다시 담기

# print(lst)
# check = ['&', '[]', '*']

# for i in range(len(lst)):
#     tmp = ''
#     cnt = 0 # 변수 길이 측정
#     for j in range(len(lst[i])-1, -1, -1): # 뒤에서부터 
#         for z in range(len(check)):
#             length = len(check[z])
#             # print(lst[i][j:j+length])
#             if check[z] == lst[i][j:j+length]: # 뒤에서 부터 check len만큼 가져와 맞는지 판별
#                 tmp += check[z]
#                 cnt = j

#     if cnt != 0: # 변수길이
#         print(f'{front}{tmp} {lst[i][0:cnt]};')
#     else:
#         print(f'{front}{tmp} {lst[i][0]};')
