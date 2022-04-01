'''
코테의 난이도
    난이도1. 문법을 알고있다
    난이도2. 알고리즘과 자료구조를 이해하고 있다.
    난이도3. 적확한 선택을 통해 문제를 풀 수 있다.
    난이도4. 코테에서 정답률 10%쯤 되는 문제를 풀 수 있다.
    난이도5. 코테 수준의 지식만 사용하지만 풀이를 떠올리기 쉽지 않고 구현 난이도도 상당한 문제를 풀 수 있다.

필수 테크닉
    정렬
    문자열 처리
    dp
    다익스트라
    BFS, DFS
    완탐
    이분탐색

높은 난이도로 나오는 알고리즘
    배열에서의 DP
    Tree에서의 DP
    투 포인터
    위상 정렬

자료구조
    Hashmap
    deque(queue)
    stack
    priority Queue
    Dynamic Array


꿀팁
    1. 문제를 올바른 순서로 이해한다.
        읽기
            시간, 메모리 제한
            문제 전체를 꼼꼼히
        이해하기
            제공되는 정보(변수들)정리
            예제 데이터에 대해 이해
        파악하기
            가능한 최대, 최소 정답에 맞는 데이터를 직접 생성
            키워드가 되는 단어들을 체크
    
    2. 시간복잡도와 공간복잡도를 계산한다.
        시간을 아끼기 : 짤 가치가 있나

    3. 코드를 효율적으로 함수화해서 구현한다.
        BAD
        First Time {
            20줄 짜리 알고리즘 (다익스트라)
        }  
        Second Time {
            20줄 짜리 알고리즘 
        }
        Tird Time {
            20줄 짜리 알고리즘
        }

        GOOD
        Dijkstra(conditions) {
           20줄 짜리 알고리즘  
        }
        First Time {
            Dijkstra(first_condition)
        }  
        Second Time {
            Dijkstra(second_condition)
        }
        Tird Time {
            Dijkstra(third_condition)
        }

    4. 부분점수를 챙긴다.
        1번에 올인하지말고 2,3번에 부분점수를 쉽게 딸 수 있다면 그것들 챙기기

             

'''