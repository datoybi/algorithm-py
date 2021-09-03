'''
    제목 : K 번째 수 
    난이도 : 중
    유형 : 정렬
    시간 : 25분
    느낀점 : 내장 sort 함수가 참 편하구나!
'''
# 맞았음 , 해답
num, order = map(int, input().split(' '))
data = []
s_data = []

data = list(map(int, input().split(' ')))
s_data = sorted(data)

print(s_data[order-1])

# 두번쨰 시도 
n, k = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
array.sort()

print(array[k-1])

