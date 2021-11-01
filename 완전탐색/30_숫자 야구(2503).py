'''
    스트라이크 : 동일한 자리, 동일한 수
    볼 : 다른 자리, 동일한 수

    N : 자연수 N, 몇번이나 질문을 했는지 (1 <= N <= 100)
    세자리수, 스트라이크, 볼
    4
    123 1 1
    356 1 0
    327 2 0
    489 0 1

    2
'''

n_lst = [123, 356, 327, 489]
s_lst = [[1, 1],[1, 0],[2, 0],[0, 1]]
whole_lst = list()

num = list('429')
answer = list('324')

print(num, answer)

for i in range(100,501):
    whole_lst.append(i)

    for j in range(3):
        if num[j] == answer[j]: # 스트라이크인지 ?
            print("스트라이크")
            break

        if num[j] in answer : # 볼인지 ?
            print("뽈")
            
print(whole_lst)


# for i in range(3):
#     if num[i] == answer[i]: # 스트라이크인지 ?
#         print("스트라이크")
#         break

#     if num[i] in answer : # 볼인지 ?
#         print("뽈")