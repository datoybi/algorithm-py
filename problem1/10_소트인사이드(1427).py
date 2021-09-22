'''
    제목 : 소트인사이드
    난이도 : 하
    유형 : 정렬, 배열
    시간 : 25분

'''
# 내 해답 

# array = list(map(int,input()))
# array.sort()
# r_array = reversed(array) # <list_reverseiterator object at 0x0000021AF3766F70>
# arr = list(r_array)

# for i in arr:
#     print(i, end='') # 개행 하지 않고 출력

#########################################################
array = list(map(int, input()))

for i in range(len(array)):
    max = i
    for j in range(i+1, len(array)):
        if array[max] < array[j]:
            max = j
    array[i], array[max] = array[max], array[i]

for i in array:
    print(i, end='')

# 해설
array = input()
for i in range(9,-1,-1): # range(start, stop, step) 마지막 인자는 숫자의 간격을 의미

    for j in array:
        if int(j) == i:
            print(i, end='')


# 두번쨰 시도 - 정답 
n = input()
n = list(map(int, n))

n.sort()
reversed_n = list(reversed(n))

reversed_n = list(map(str,reversed_n))

for i in reversed_n:
    print(i, end='')

