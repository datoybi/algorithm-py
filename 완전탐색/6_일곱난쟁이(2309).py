# 키 , 100미만 자연수 키 , 모두 다름 , 여러가지인 경우 아무거나 출력 
# 일곱 난쟁이의 키의 합 = 100 
# 힌트를 얻었음 ! 2개뺴고 다 더한값이 100이라고 가정 하기
lst = list()

for _ in range(0,9):
    lst.append(int(input()))
lst.sort()

for i in range(8, 0, -1): # 8-1
  for j in range(7,-1,-1): # 7-0
    result = sum(lst[0:]) - lst[i] - lst[j]
    #print(result)
    if result == 100:
      del lst[i], lst[j]
      for z in lst:
        print(z)
      exit(0)