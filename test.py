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
'''
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

import sys
a, b = list(map(int, sys.stdin.readline().split()))
print(b * 2 - a)

