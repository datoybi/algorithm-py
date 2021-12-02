'''
문제 뭔말이냐.. 
아놔.. 제일 끝에 있는 두 개의 염기를 양 끝으로 이해했는데 그게 아니고!!!! 
len(A)-1,len(A)-2를 말한거였다.

'''
import sys

decoder = {
    'A': {'A': 'A', 'G': 'C', 'C': 'A', 'T': 'G'},
    'G': {'A': 'C', 'G': 'G', 'C': 'T', 'T': 'A'},
    'C': {'A': 'A', 'G': 'T', 'C': 'C', 'T': 'G'},
    'T': {'A': 'G', 'G': 'A', 'C': 'G', 'T': 'T'}
}

n = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()

for _ in range(n-1):
    new = decoder[word[-1]][word[-2]]
    word = word[:-2] + new

print(word)


# 메모리 초과

# import sys

# n = int(sys.stdin.readline())
# lst = list(sys.stdin.readline().rstrip())

# while True:
#     if len(lst) == 1: break
#     tmp = list()
#     tmp.append(lst[-1])
#     tmp.append(lst[-2])
#     tmp.sort()
#     result = ''

#     if tmp[0] == tmp[1]:
#         result = tmp[0]

#     elif tmp[0] == 'A' and tmp[1] == 'G':
#         result = 'C'

#     elif tmp[0] == 'A' and tmp[1] == 'C':
#         result = 'A'
        
#     elif tmp[0] == 'A' and tmp[1] == 'T':
#         result = 'G'
    
#     elif tmp[0] == 'C' and tmp[1] == 'G':
#         result = 'T'

#     elif tmp[0] == 'C' and tmp[1] == 'T':
#         result = 'G'

#     elif tmp[0] == 'G' and tmp[1] == 'T':
#         result = 'A'

#     del lst[-1]
#     del lst[-1]
#     lst.append(result)

# print(lst[0])