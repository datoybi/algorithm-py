'''
    제목 : 공유기 설치 
    난이도 : 중
    유형 : 이진 탐색 
    시간 : 40분
    이진탐색이 들어가면 어느정도 구현도 까다롭고 다소 개념적으로 어려운 문제가 출제될 가능성이 높다.
    문제 풀이 핵심 아이디어
        집의 개수 N은 최대 200,000 이며, 집의 좌표 X는 최대 1,000,000,000입니다.
        이진 탐색을 이용하여 O(N*logX)에 문제를 해결할 수 있습니다.
        가장 인접한 두 공유기 사이의 최대 Gap을 이진 탐색으로 찾습니다.

    이해 안됌ㅠㅠ씨빨...
'''

n, c = list(map(int, input().split(' ')))
array = []

for _ in range(n):
    array.append(int(input()))
array = sorted(array)

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while(start <= end):
    mid = (start + end) // 2 # 정수 부분만 구함 mid 는 gap을 의미합니다
    value = array[0]
    count = 1

for i in range(1, len(array)):
    if array[i] >= value + mid:
        value = array[i]
        count += 1

if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우
    start = mid + 1
    result = mid
else: # C개 이상의 공유기를 설치할 수 없는 경우
    end = mid - 1

print(result)



