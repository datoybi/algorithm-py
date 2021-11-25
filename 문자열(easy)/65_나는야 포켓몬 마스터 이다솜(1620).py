'''
포켓몬 개수 N 맞춰야하는 문제의 개수 M
1 <= N,M <= 100,000
N개의 줄의 포켓몬의 번호가 1번부터 N번까지 (첫 글자만 대문자 나머지문자 소문자 , 마지막문자만 대문자일수도 있음)
이름은 2~20 글자
M 개의 내가 맞춰야하는 문제 (알파벳-> 포켓몬 번호, 숫자 -> 이름) 1 <= 문제 

# 처음에 시간초과가 났다. dictinary 반복문을 돌리니까 십만번의 데이터가 있을 때 시간이 초과되는 것 같다.
그래서 딕셔너리를 하나 더 만들어서 문제가 숫자와 문자인 경우를 각각 다른 딕셔너리로 판별해주었다.
'''

import sys

N, M = map(int, sys.stdin.readline().split())
book_n, book_s = dict(), dict()

# dict에 담기
for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    book_n[i+1] = tmp
    book_s[tmp] = i+1

# print(book_n)
# print(book_s)

# 판별
for j in range(M):
    input_val = sys.stdin.readline().rstrip()
    
    if input_val.isdigit(): # 숫자면
        print(book_n[int(input_val)])
    else:
        print(book_s[input_val])


