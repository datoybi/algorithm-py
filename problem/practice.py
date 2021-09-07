books = {}
n = int(input())
arranged = list()

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
    target = max(books.values())
    
    for book, number in books.items():
        if number == target:
            arranged.append(book)

print(sorted(arranged)[0])