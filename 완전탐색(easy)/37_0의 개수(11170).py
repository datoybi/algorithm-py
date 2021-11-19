'''
맞았습니다!
3
0 10
33 1005
1 4

2
199
0

'''
T, lst = int(input()), list()

for i in range(T):
    lst.append(list(map(int, input().split())))

print(lst) # [[0, 10], [33, 1005], [1, 4]]
# print(lst[0])

for t in range(T):
    count = 0
    for i in range(lst[t][0], lst[t][1]+1):
        tmp = list(str(i))
        for j in range(len(tmp)):
            if tmp[j] == '0': # 왜 이건 안되고 그 아래꺼는 될까요.... 50퍼에서 멈추는거 보니까 뭔가... 어떤 특정 테스트케이스를 통과하지 못하는 것 같다.. 그게뭔지 몰그ㅔㅆ지만 ㅠㅠ
                # print(tmp, count)
                count+=1
    print(count)


# for t in range(T):
#     count = 0
#     for i in range(lst[t][0], lst[t][1]+1):
#         tmp = list(str(i))
#         count += tmp.count('0')
       
#     print(count)


# 남 코드 -> 훨씬 간결하다.
x = int(input())
for i in range(x):
    count = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        w = str(i)
        count += w.count('0')
    print(count)