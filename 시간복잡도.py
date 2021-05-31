'''
    시간복잡도 : 알고리즘 실행 속도
    공간복잡도 : 알고리즘이 사용하는 메모리 사이즈

    빅 오 표기법 
    O (입력)
    입력 n에 따라 결정되는 시간 복잡도 함수 
    O(1), O(logn), O(n), O(nlogn), O(n제곱), O(2승), O(n!)
    입력 n의 크기에 따라 기하급수적으로 시간 복잡도가 늘어날 수 있음
    O(1) < O(logn) < O(n) < O(nlogn) < O(n제곱) < O(2승) < O(n!)
        참고 : log n의 베이스는 2-log2n
    
    단순하게 입력 n에 따라, 몇번 실행이 되는지를 계산하면 된다.
        표현식에 가장 큰 영향을 미치는 n의 단위로 표기한다. n은 입력값ㅌ
        n이 1이든 100이든, 1000이든, 10000이든 실행을 
        무조건 2회(상수회) 실행한다 -> O(1)
        n에 따라 n번, n+10번, 또는 3n+10 번 등 실행한다. O(n)
        n에 따라 n제곱번, n제곱+1000번, 또는 100파이제곱 -100번 등을 실행한다. O(파이제곱)
    
    빅오 입력값 표기 방법
        가장 높은 차수 표기 
'''
'''
 알고리즘1 : 1부터 n까지 합을 구하는 알고리즘1
    합을 기록할 변수를 만들고 0을 저장 
    n을 1부터 1씩 증가하면서 반복
    반복문 안에서 합을 기록할 변수에 1씩 증가된 값을 더함 
    반복이 끝나면 합을 출력
'''
# O(n)
def sum(n):
    total = 0
    for num in range(1, n+1):
        total += num
    return total
        
print(sum(100))

# 알고리즘2: 1부터 n까지의 합을 구하는 알고리즘2 O(1)
def sum(n):
    return int(n*(n+1)/2)

print(sum(100))


'''
    0(1) : 입력 데이터가 상관없이 일정한 시간이 걸리는 알고리즘 
    f(int[] n) {
        return (n[0] == 0) ? true: false;
    }

    O(n) : 입력 데이터의 크기에 비례하여 처리시간이 걸리는 알고리즘
    f(int[] n) {
        for i = 0 to n.length
        print i
    }

    O(n2) : n에서 또 n루프를 돌릴때 처리시간이 걸리는 알고리즘
    f(int[] n) {
        for i = 0 to n.length
            for j = 0 to n.length
                print i + j;
    }

    O(nm) : n에서 m 루프를 돌리는 알고리즘
    f(int[] n, int[] m) {
        for i = 0 to n.length
            for j = 0 to m.length
                print i + j;
    }

    O(n3) : 루프안에 또 루프, 또 루프가 있는 알고리즘 
    f(int[] n) {
        for i = 0 to n.length
            for j = 0 to n.length
                for k = 0 to n.length
                    print i + j + k;
    }

    O(2n승) : 피보나치 수열
    f(n, r) {
        if (n <= 0) return 0;
        else if(n == 1) return r[n] = 1;
        return r[n] = f(n-1, r) + f(n-2, r);
    }

    O(log n) : 이진 검색(binary search)
    f(k, arr, s, e){
        if(s > e) return -1;
        m = (s + e) / 2;
        if(arr[m] == k) return m;
        else if (arr[m] > k) return f(k, arr, s, m-1);
        else return f(k, arr, m+1, e);
    }

    O(sqrt(n)) : 제곱근 



'''