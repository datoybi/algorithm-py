'''
어캐접근해야할까..
L보다 크거나 같고 R보다 작거나 같은 자연수중 8이 가장 적게 들어있는 수
에 들어있는 8의 개수를 구하시오
데이터 이십억이니까 계산 잘 하자;; 
808 808
2
128 138
0
1887 1888
2
883802 8838

'''
import sys

n, m =  sys.stdin.readline().split()
cnt = 0

if len(n) == len(m):
    for i in range(max(len(n), len(m))):
        if n[i] == m[i] and n[i] =='8':
            cnt += 1
        elif n[i] != m[i]:
            break

print(cnt)