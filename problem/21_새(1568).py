'''
    제목 : 새
    난이도 : 하
    유형 : 탐색
    시간 : 20분
    문제가 뭔말인지 이해 못하겠음 ㅠ
'''

'''
    문제 풀이 핵심 아이디어
        N이 최대 1,000,000,000입니다
        K가 반복적으로 증가하므로, 날아가는 새의 마리 수는 빠르게 증가합니다.
        따라서 문제에서 요구하는 대로 단순히 구현하여 정답 처리를 받을 수 있습니다.
'''

# bird = int(input())
# result = 0
# index = 1

# while(bird): # 0이 되면 나가짐
#     bird = bird-index
#     result+=1
#     # print(index , bird)
#     if bird < index+1:
#         index = 1
#     else:
#         index+=1

# print(result)


# 해답
n = int(input())
result = 0
k = 1
while n != 0:
    if k>n:
        k=1
    n -= k
    k += 1
    result +=1
print(result)