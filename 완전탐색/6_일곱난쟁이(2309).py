# 키 , 100미만 자연수 키 , 모두 다름 , 여러가지인 경우 아무거나 출력 
# 일곱 난쟁이의 키의 합 = 100 
# 힌트를 얻었음 ! 2개뺴고 다 더한값이 100이라고 가정 하기


lst = list()
test = list()
add = 0
selected

for _ in range(0,9):
    lst.append(int(input()))
lst.sort()

    print(sum(lst[0:7]))

# for i in lst:   
    
    # if sum(lst[0:7]) == 100:
    # print(sum(lst[0:7]))
    # add += i
    # if add < 100:
    #     add += i
    # elif add > 100:
    #     add += i
    # elif add == 100:
    #     print(test)