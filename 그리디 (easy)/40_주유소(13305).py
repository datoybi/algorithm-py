# 맞았습니다!
'''
5
2 3 1 1
5 2 4 1 1

19
'''
import sys

int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
station = list(map(int, sys.stdin.readline().split()))
price, min_station = 0, station[0]
del station[-1]

for i in range(len(station)):
    min_station = min(min_station, station[i])
    price += road[i] * min_station
print(price)