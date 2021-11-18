'''
맞았습니다!
종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수
1 666
2 1666
3 2666
4 3666
187 66666
500 166699
N은 10,000보다 작거나 같은 자연수
'''

count = 0
N = int(input())

for i in range(665, 2666800): # N이 10000일때 2666799
    if '666' in str(i):
        count += 1
        # print(i, count)
        if count == N:
            print(i)
            exit(0)
# print(count)
