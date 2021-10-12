# 맞았습니다!

T = int(input())

for i in range(T):
    n, m = map(int, input().split(' '))
    result = 0
    b = n-1
    for a in range(1, b):
        for b in range(2, n):
            if a < b:
                if (a*a+b*b+m)%(a*b) == 0:
                    # print('a ' , a ,'b ' , b)
                    # print("정수입니다")
                    result = result+1

    print(result)
