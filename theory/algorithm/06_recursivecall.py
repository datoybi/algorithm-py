'''
    재귀 용법 (recursive call)
        고급 정렬 알고리즘에서 재귀 용법을 사용하므로, 고급 정렬 알고리즘을 익히기 전에 재귀 용법을 먼저 익히기로 합니다.

        함수 안에서 동일한 함수를 호출하는 형태 
        여러 알고리즘 작성시 사용되므로, 익숙해져야 함
'''

# 팩토리얼을 구하는 알고리즘을 Recursive Call을 활용해서 알고리즘 작성하기
'''
    분석하기
        2! = 1x2
        3! = 1x2x3
        4! = 1x2x3x4

        규칙
            n! = n x (n-1)!
            함수(n)은 n>1이면 return nX함수(n-1)
            함수(n)은 n=1이면 return n

        검증
            코드로 검증하지말고, 직접 간단한 경우부터 대입해서 검증해야 함
        
        시간복잡도/ 공간복잡도는 O(n-1)이므로 결국 둘다 O(n)
            
'''
def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    else:
        return num

for num in range(10):
    print(factorial(num))


'''
재귀 호출의 일반적인 형태 

    def function(입력):
        if 입력 > 일정값: # 입력이 일정 값 이상이면 
            return function(입력-1) # 입력보다 작은 값
        else:
            return 일정값, 일정값 또는 특정값 # 재귀 호출 종료

    # 일반적인 형태2
    def function(입력):
        if 입력 <= 일정값: # 입력이 일정 값보다 작으면
            return 일정값, 일정값 또는 특정값 # 재귀 호출 종료
        function(입력보다 작은 값)
        return 결과값

'''

def factorial(num):
    if num <= 1:
        return num
    return_value = num * factorial(num-1)
    return return_value
    
for num in range(10):
    print(factorial(num))

'''
    재귀 호출은 스텍의 전형적인 예
        함수는 내부적으로 스텍처럼 관리한다.

'''