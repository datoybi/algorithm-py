#맞왜틀!!!!!!!!!!!

mushrooms = list()

for _ in range(10):
    mushrooms.append(int(input()))

pre_score = sum(mushrooms[0:9])

for j in range(0, 10):# 0-9
    score = sum(mushrooms[0:j])
    if abs(100 - score) == 0 :
        pre_score = score
        break
    elif abs(100 - pre_score) > abs(100 - score):
        pre_score = score
    elif abs(100 - pre_score) == abs(100 - score) and pre_score < score:
        pre_score = score


print(pre_score)

# import sys

# scores = 0
# for _ in range(10):
#     score = int(sys.stdin.readline())
#     pre_scores = scores
#     scores += score
#     if scores >= 100:
#         if abs(100-scores) > abs(100-pre_scores):
#             scores = pre_scores
#         break
# print(scores)

