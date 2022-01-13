'''
맞았습니다!
특정 음식을 먹을 때마다 스티커를 하나씩 제공 
스티커를 모으면 상금으로 교환 가능
여러번 교환 가능
상금 교환에 필요없는 스티커도 있다

보통 상품 금액이 큰것부터 마이너스하기 

'''
import sys

for i in range(int(sys.stdin.readline())):
    n, m = list(map(int, sys.stdin.readline().split())) # 상금의 갯수, 스티커의 종류
    price = list()

    for i in range(n):
        price.append(list(map(int, sys.stdin.readline().split())))
        del price[i][0]
    sticker = list(map(int, sys.stdin.readline().split()))
    price = sorted(price, key=lambda x:-x[-1])

    i = 0
    result = 0
    cnt = 0
    while True:
        # print(result, sticker, i)
        # print('cnt : ' , cnt)
        flag = True
        if cnt > n: break
        if i >= n:
            i=0

        for j in range(len(price[i])-1):
            if sticker[price[i][j]-1] <= 0:
                flag = False

        if flag == True:
            for j in range(len(price[i])-1):
                sticker[price[i][j]-1] -= 1
            result += price[i][-1]
            i = 0
            cnt = 0
        else:
            i += 1
            cnt += 1

    print(result)



