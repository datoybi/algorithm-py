'''
맞았습니다!
문제 해석
소가 젖을 짜는 시간동안 있는데 그 시간안에 얼마나 많은 버킷이 필요한지 구하기

        N 소 ( 1 <= N <= 100) 1~N
        i번째 소는 Si~Ti까지의 시간이 필요하고 bi 버킷을 필요로 한다.
        여러 소가 동시에 젖을 짤 수 있는데 그러면 같은 버킷을 사용할 수 없다.
        그러니까 소 i가 젖을 짤 때 버킷을 사용하고 있으면 다른 소들은 Si~Ti 동안엔 버킷을 사용할 수 없다 

        농부는 버킷을 오름차순으로 레이블을 붙인다. 어떤 소가 젖을 짜기 시작하면 농부는 버킷을 가져와서 라벨을 할당한다
        모든 소가 전부 젖을 짜려면 얼마나 많은 버킷이 필요한지 구하시오 

        N 소의 수 
        s t b 
        s: 시작시간
        t: 끝시간
        b: 필요한 버킷개수 

'''
import sys

time = [0 for _ in range(1001)]

for _ in range(int(sys.stdin.readline())):
    s, t, b = list(map(int, sys.stdin.readline().split()))

    for i in range(s, t+1):
        time[i] += b

print(max(time))