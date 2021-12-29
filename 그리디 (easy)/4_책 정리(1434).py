'''
맞았습니다!
뭔말이야......문제가 넘 모호하다 짜증;;

박스의 개수 N 책의 개수 M
박스의 용량 
책의 크기

'''
import sys

N, M = list(map(int, sys.stdin.readline().split()))
boxes = list(map(int, sys.stdin.readline().split()))
books = list(map(int, sys.stdin.readline().split()))
book_idx, box_idx = 0, 0

while True:
    if box_idx >= N or book_idx >= M:
        break
    if books[book_idx] <= boxes[box_idx]:
        boxes[box_idx] = boxes[box_idx] - books[book_idx]
        book_idx += 1
    else:
        box_idx += 1

print(sum(boxes))