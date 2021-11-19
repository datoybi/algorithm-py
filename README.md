# Datastructure-and-Algorithm
*코딩테스트 준비를 위한 알고리즘&자료구조 연습*<br>
*fast campus의 "알고리즘 / 기술면접 완전 정복 올인원 패키지 Online" 수강*


## 🔷Python 문법 정리🔷
### 계속 정리해 나갈 예정 (마지막 업데이트: 21.08.31)


🔹 range(start, stop, step) 마지막 인자는 숫자의 간격을 의미 
    <pre><code>  for i in range(9,-1,-1): # 9~0 
	for i in range(0,5): # 0,1,2,3,4</pre></code>

🔹 개행 없이 프린트 
    <pre><code>print(i, end='')</code></pre>

🔹 swap 
    <pre><code>array[i], array[max] = array[max], array[i]</code></pre>

🔹 개행 한번 하고 프린트 하고싶을때 
	<pre><code>print('\n'.join(result))</code></pre>

🔹 정렬 
    <pre><code>  list.sort() 
    sorted(list) </code></pre>

🔹 역정렬 
    reversed는 순서를 뒤집어 주는거기 때문에 sort하고 reverse 쳐야함
    <pre><code> r_answer = list(reversed(answer)) #list()에 감싸야한다</code></pre>

🔹 lambda 인자 : 표현식 
    <pre><code>  (lambda x,y : x+y)(10, 20) # 30 
    array = sorted(array, key=lambda x:x[0]) </code></pre>

* 튜플 ? 
    > 리스트는 []으로 둘러싸지만 튜플은 ()으로 둘러싼다.<br>
    > 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다. 

* sys.stdin.readline() 
    > 데이터의 개수가 많을 때 파이썬에서는 sys.stdin.readline()을 사용 

🔹 3개의 변수에 입력값 할당 
    <pre><code> n, r, c = map(int, input().split(' ')) </code></pre>

🔹 list에 int형 input value 넣기 
    <pre><code> data = list(map(int, input().split(' '))) </code></pre>

🔹 두 변수에 int형 input 넣을때  
    <pre><code> num, order = map(int, input().split(' ')) </code></pre>

🔹 while문 
    <pre><code>hile(bird): # 0이 되면 나가짐 </code></pre>

🔹 max()
    🔹 최대값을 찾는 내장함수
    <pre><code> max([1, 2, 3]) # 3
    max(10, 20) # 20</code></pre>


🔹 X in S, X not in S 
	> X in S : S안에 X가 있다면 참 <br>
	> X not in S : S안에 X가 없다면 참 (이때 S는 리스트, 튜플, 문자열)

* Set
	> 중복을 허용하지 않는다.<br>
	> 순서가 없다. (리스트나 튜플은 순서가 있다)<br>
	> ```set2 = set('Hello')```<br>
	> ```set2 # {'e', 'H', 'l', 'o'}```<br>
	> -> Set 자료형에 인덱싱으로 접근하려면, 튜플로 변환 한 후 접근해야 한다<br> 
	>```(s1 > = set([1,2,3]) l1 = list(s1))```<br><br>
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
	
	 *reference : https://wikidocs.net/1015*

🔹 문자열을 한글자씩 끊어서 리스트로 바꾸기 
	<pre><code>  str = "hello"
	print(list(str))</code></pre>

🔹	변수 출력시 공백 제거하고싶을 떄 
	<pre><code>print("Cube = ",a,", Triple = (",b,",",c,",",d,")", sep="")
	print(f"Cube = {a}, Triple = ({b},{c},{d})")</code></pre>


🔹 람다식
	<pre><code>  def hap(x, y):
	return x+y
	print(hap(10,20))</code></pre>

🔹 lambda 매개변수 : 실행문<br>
	<pre><code>  print((lambda x,y: x+y)(10, 20))
	func = (lambda x: x+1)
	print(func(4)) #5</code></pre>

🔹 input() 보다 sys.stdin.readline()이 좀 더 빠르고 메모리도 적게 소모한다.
🔹 array를 0으로 채우기
  <pre><code>    test[0] * 10 // [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  	array[0] * 10001 </code></pre>

🔹 Python3는 pypy3보다 느리다, pypy3는 Python3보다 빠르지만 메모리를 많이 먹는다.

🔹 dictionary
* 기본 모습 
	* key : value 쌍으로 이루어져 있음
<pre><code> dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}</code></pre>
* 쌍 추가 
<pre><code>a = {1: 'a'}
a[2] = 'b'
a # {1: 'a', 2: 'b'}</code></pre>
* 삭제
<pre><code>del a[1]</code></pre>
* key를 사용해 value 얻기
<pre><code>grade = {'pey': 10, 'julliet': 99}
grade['pey'] # 10
grade['julliet'] # 99</code></pre>

* 반복문 사용

<pre><code>for book, number in books.items(): # key, value 반복문
if number == target: 
arranged.append(book)
# target = max(books.values())

</code></pre>

* 주의사항 
	* key는 고유값이므로 중복되는 key값을 설정해 놓으면 나머지 것들이 모두 무시된다는점을 주의해야한다.


🔹 승 구하기
 <pre><code>print(2**3) #2*2*2=8</code></pre>


🔹 문자열 뒤집기
 <pre><code>s = '61'
print(s[::-1]) # 16</code></pre>

for key, value in result.items():
    if value == max(result.values()):
        print(key)

	람다 배우기 max_val = max(t[1] for t in result_lst)


🔹 순열 (permutation)
몇개를 골라 순서를 고려해 나열한 경우의 수
예)1,2,3의 숫자가 적힌 카드가 있을 때, 이 중 두 장을 꺼내는 경우의 수 -> 12, 13, 21, 23, 31, 32
'A', 'B', 'C'로 만들 수 있는 경우의 수 -> 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

사용법 

<pre><code>import itertools
arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 3)
print(list(nPr))
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
#['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
#['AB', 'AC', 'BA', 'BC', 'CA', 'CB']</pre></code>

for문 안의 permutation 
<pre><code>
import itertools

lst = ['1', '2', '3']

print(list(itertools.permutations(lst, 2)))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
for i in itertools.permutations(lst, 2):
    print(i)
    # ('1', '2')
    # ('1', '3')
    # ('2', '1')
    # ('2', '3')
    # ('3', '1')
    # ('3', '2')

    print(''.join(i))
    # 12
    # 13
    # 21
    # 23
    # 31
    # 32

</pre></code>

람다함수
인자 : 표현식
lst = [
        [55, 185],
        [58, 183],
        [88, 186],
        [60, 175],
        [46, 155]
    ]

func = sorted(lst, key = lambda x : [-x[0], -x[1]])

sorted -> 정렬 
lst 라는 이중 리스트에
-x : 내림차순으로 정렬
x : 오름차순으로 정렬


0인 원소의 list 만들기
zero_lst = [0 for _ in range(130)]

sys.stdin.readline()

impoty sys

한개입력
a = int(sys.stdin.readline())
: 3을 입력하면 3\n이렇게 입력이 되기 때문에 형변환을 거쳐야 함

여러개 입력 
a,b,c = map(int, sys.stdin.readline().split())

리스트에 저장 
int
data = list(map(int, sys.stdin.readline().split()))

문자열 
value = list(map(str, sys.stdin.readline().split()))
value = sys.stdin.readline().split()


2차원 리스트에 저장
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

문자열 n줄을 입력받아 리스트에 저장 
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

개행 없애기 
strip() 붙이기
word_lst.append(sys.stdin.readline().strip())
