"""
    제목 : 베스트셀러
    난이도 : 하
    유형 : 탐색
    시간 : 20분
    문제 풀이 핵심 아이디어 
        본 문제는 가장 많이 등장한 문자열을 출력하는 문제와 동일합니다.
        등장 횟수를 계산할 때는 파이썬의 Dictionary 자료형을 이용하면 효과적입니다.
    느낀점 : 비슷하게 구현하려고 했는데 문법을 어떻게 사용하지는 지 몰라서 버벅 거렸다. 방법론은 거의 유사했다.
    
"""

n = int(input())
books = {} # dictionary

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
    target = max(books.)
    array = []

    for book, number in books.items():
        if number == target:
            array.append(book)

print(sorted(array)[0])