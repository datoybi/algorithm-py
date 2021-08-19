# Datastructure-and-Algorithm
study Data structure and Algorithm with fast campus
<br>
## Phython 문법 정리
### 계속 정리해 나갈 예정 (마지막 업데이트: 21.08.19)

- range(start, stop, step) 마지막 인자는 숫자의 간격을 의미 
for i in range(9,-1,-1): # 9~0 

for i in range(0,5): # 0,1,2,3,4 

- 개행 없이 프린트 
print(i, end='') 

- sawp 
array[i], array[max] = array[max], array[i] 

- 개행 한번 하고 프린트 하고싶을때 
print('\n'.join(result)) 

- 정렬 
list.sort() 
sorted(list) 

- lambda 인자 : 표현식 
(lambda x,y : x+y)(10, 20) # 30 
array = sorted(array, key=lambda x:x[0]) 

- 튜플 ? 
 - 리스트는 []으로 둘러싸지만 튜플은 ()으로 둘러싼다. 
 - 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다. 

- sys.stdin.readline() 
데이터의 개수가 많을 때 파이썬에서는 sys.stdin.readline()을 사용 

- 3개의 변수에 입력값 할당 
n, r, c = map(int, input().split(' ')) 

- list에 int형 input value 넣기 
data = list(map(int, input().split(' '))) 

- 두 변수에 int형 input 넣을때  
num, order = map(int, input().split(' ')) 

* while문 
while(bird): # 0이 되면 나가짐 


