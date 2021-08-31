# Datastructure-and-Algorithm
study Data structure and Algorithm with fast campus

## Python 문법 정리
### 계속 정리해 나갈 예정 (마지막 업데이트: 21.08.30)


* range(start, stop, step) 마지막 인자는 숫자의 간격을 의미 
    <pre><code>  for i in range(9,-1,-1): # 9~0 
	for i in range(0,5): # 0,1,2,3,4</pre></code>

* 개행 없이 프린트 
    <pre><code>print(i, end='')</code></pre>

* swap 
    <pre><code>array[i], array[max] = array[max], array[i]</code></pre>

* 개행 한번 하고 프린트 하고싶을때 
	<pre><code>print('\n'.join(result))</code></pre>

* 정렬 
    <pre><code>  list.sort() 
    sorted(list) </code></pre>

* 역정렬 
    <pre><code> r_answer = list(reversed(answer)) #list()에 감싸야한다</code></pre>

* lambda 인자 : 표현식 
    <pre><code>  (lambda x,y : x+y)(10, 20) # 30 
    array = sorted(array, key=lambda x:x[0]) </code></pre>

* 튜플 ? 
    > 리스트는 []으로 둘러싸지만 튜플은 ()으로 둘러싼다.<br>
    > 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다. 

* sys.stdin.readline() 
    > 데이터의 개수가 많을 때 파이썬에서는 sys.stdin.readline()을 사용 

* 3개의 변수에 입력값 할당 
    <pre><code> n, r, c = map(int, input().split(' ')) </code></pre>

* list에 int형 input value 넣기 
    <pre><code> data = list(map(int, input().split(' '))) </code></pre>

* 두 변수에 int형 input 넣을때  
    <pre><code> num, order = map(int, input().split(' ')) </code></pre>

* while문 
    <pre><code>hile(bird): # 0이 되면 나가짐 </code></pre>

* max()
    * 최대값을 찾는 내장함수
    <pre><code> max([1, 2, 3]) # 3
    max(10, 20) # 20</code></pre>


* X in S, X not in S 
	> X in S : S안에 X가 있다면 참 <br>
	> X not in S : S안에 X가 없다면 참 (이때 S는 리스트, 튜플, 문자열)

* Set
	> 중복을 허용하지 않는다.<br>
	> 순서가 없다. (리스트나 튜플은 순서가 있다)<br>
	> set2 = set('Hello')<br>
	> set2 # {'e', 'H', 'l', 'o'}<br>
	> -> Set 자료형에 인덱싱으로 접근하려면, 튜플로 변환 한 후 접근해야 한다<br> (s1 > = set([1,2,3]) l1 = list(s1))<br><br>
	> set자료형으로 교집합 구하기 ```(s1 & s2)```<br>
	> set자료형으로 합집합 구하기 ```(s1 | s2)```<br>
	> set자료형으로 차집합 구하기 ```(s1 - s2)```<br>
	>	> 값추가 (add) <br>
 	>	>	>		s1 = set([1, 2, 3]) 
	>	>	>		s1.add(4)
	>	>	>		s1 # {1, 2, 3, 4}
	>	>  값 여러개 추가하기 (update)<br>
 	>	>	>		s1 = set([1, 2, 3])
 	>	>	>		s1.update([4, 5, 6])
 	>	>	>		s1 # {1, 2, 3, 4, 5, 6}
	>	>  특정 값 제거하기 (remove)<br>
 	>	>	>		s1 = set([1, 2, 3])
 	>	>	>		s1.remove(2)
 	>	>	>		s1 # {1, 3}
	
	reference : https://wikidocs.net/1015

* 문자열을 한글자씩 끊어서 리스트로 바꾸기 
	<pre><code>  str = "hello"
	print(list(str))</code></pre>

* 람다식
	<pre><code>  def hap(x, y):
	return x+y
	print(hap(10,20))</code></pre>

* lambda 매개변수 : 실행문<br>
	<pre><code>  print((lambda x,y: x+y)(10, 20))
	func = (lambda x: x+1)
	print(func(4)) #5</code></pre>

* input() 보다 sys.stdin.readline()이 좀 더 빠르고 메모리도 적게 소모한다.
* array를 0으로 채우기
  <pre><code>    test[0] * 10 // [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  	array[0] * 10001 </code></pre>

* Python3는 pypy3보다 느리다, pypy3는 Python3보다 빠르지만 메모리를 많이 먹는다.