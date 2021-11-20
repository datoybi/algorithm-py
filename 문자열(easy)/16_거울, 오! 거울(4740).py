# # 맞았습니다
# import sys
# 이 방법으로 푼사람 1명도 없다 왜안되는지 모를...
# while True:
#     word = sys.stdin.readline().rstrip()
#     print(word)
#     if word == '***':
#         exit(0)

#     answer = ''
#     for i in range(len(word)-1, -1, -1):
#         answer += word[i]
#     print(answer)

while True:
    word = input()
    if word == '***':
        exit(0)

    print(word[::-1])