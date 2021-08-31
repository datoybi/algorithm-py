# Datastructure-and-Algorithm
study Data structure and Algorithm with fast campus

## Python 문법 정리
### 계속 정리해 나갈 예정 (마지막 업데이트: 21.08.30)
--------

* range(start, stop, step) 마지막 인자는 숫자의 간격을 의미 
    <pre><code>  for i in range(9,-1,-1): # 9~0 
	for i in range(0,5): # 0,1,2,3,4</pre></code>

* 개행 없이 프린트 
    <pre><code>print(i, end='')</code></pre>

* swap 
    <pre><code>array[i], array[max] = array[max], array[i]</code></pre>

* 개행 한번 하고 프린트 하고싶을때 
       ```print('\n'.join(result)) ```

* 정렬 
    * list.sort() 
    * sorted(list) 

* 역정렬 
    * r_answer = list(reversed(answer)) # list()에 감싸야한다

* lambda 인자 : 표현식 
    * (lambda x,y : x+y)(10, 20) # 30 
    * array = sorted(array, key=lambda x:x[0]) 

* 튜플 ? 
    * 리스트는 []으로 둘러싸지만 튜플은 ()으로 둘러싼다. 
    * 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다. 

* sys.stdin.readline() 
    * 데이터의 개수가 많을 때 파이썬에서는 sys.stdin.readline()을 사용 

* 3개의 변수에 입력값 할당 
    * n, r, c = map(int, input().split(' ')) 

* list에 int형 input value 넣기 
    * data = list(map(int, input().split(' '))) 

* 두 변수에 int형 input 넣을때  
    * num, order = map(int, input().split(' ')) 

* while문 
    * hile(bird): # 0이 되면 나가짐 

* max()
    * 최대값을 찾는 내장함수
    * max([1, 2, 3]) # 3
    * max(10, 20) # 20


* X in S, X not in S 
	* X in S : S안에 X가 있다면 참 
	* X not in S : S안에 X가 없다면 참 (이때 S는 리스트, 튜플, 문자열)

* Set
	* 중복을 허용하지 않는다.
	* 순서가 없다. (리스트나 튜플은 순서가 있다)
	set2 = set('Hello')
	set2 # {'e', 'H', 'l', 'o'}
	-> Set 자료형에 인덱싱으로 접근하려면, 튜플로 변환 한 후 접근해야 한다 (s1 = set([1,2,3]) l1 = list(s1))
	* set자료형으로 교집합 구하기 (s1 & s2)
	* set자료형으로 합집합 구하기 (s1 | s2)
	* set자료형으로 차집합 구하기 (s1 - s2)
	* 값추가 (add) 
 		s1 = set([1, 2, 3]) 
		s1.add(4)
		s1 # {1, 2, 3, 4}
	* 값 여러개 추가하기 (update)
		s1 = set([1, 2, 3])
		s1.update([4, 5, 6])
		s1 # {1, 2, 3, 4, 5, 6}
	* 특정 값 제거하기 (remove)
		s1 = set([1, 2, 3])
		s1.remove(2)
		s1 # {1, 3}
	
	reference : https://wikidocs.net/1015

* 문자열을 한글자씩 끊어서 리스트로 바꾸기 
	str = "hello"
	print(list(str))

* 람다식
def hap(x, y):
    return x+y

print(hap(10,20))

* lambda 매개변수 : 실행문
print((lambda x,y: x+y)(10, 20))

func = (lambda x: x+1)
print(func(4)) #5

* input() 보다 sys.stdin.readline()이 좀 더 빠르고 메모리도 적게 소모한다.
* array를 0으로 채우기
  * test[0] * 10 // [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  * array[0] * 10001 

* Python3는 pypy3보다 느리다, pypy3는 Python3보다 빠르지만 메모리를 많이 먹는다.