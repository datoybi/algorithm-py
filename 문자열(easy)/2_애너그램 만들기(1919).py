''''
맞았습니다!

abbcccddddeeeee
eddcccbbbbaaaaa

12

abb
ab

1

'''
import sys

str1, str2 = sys.stdin.readline().strip(), sys.stdin.readline().strip()
zero_list = [0 for _ in range(130)]

# 첫번째 문장의 각각의 문자들의 아스키 코드 값만큼 배열에 저장 
for i in range(len(str1)): 
    zero_list[ord(str1[i])] += 1

# 두번째 문장의 각각의 문자들의 아스키 코드 값만큼 - 해주기
for i in range(len(str2)):
    zero_list[ord(str2[i])] -= 1

answer = 0
for i in range(len(zero_list)):
    if zero_list[i] != 0: # 0 이 아니라면 절대값으로 개수 표출
        answer += abs(zero_list[i])

print(answer)