'''
맞았습니다!
어려워,,ㅠ 
https://st-lab.tistory.com/145 
이거 참고 하고 풀음.. 이런 경우에는 (X[0], X[1]) 
X[1]로 정렬를 해야한다(종료시간으로 정렬) 그런 다음에 X[0]을 오름차순 해야한다.
종료시간 증가 순 정렬, 종료시간 같으면, 시작 시간 큰 순으로

5
6 7
6 6
5 6
5 5
7 7
5

3
1 3
8 8
4 8
3

6
1 1
1 2
2 2
3 3
2 3
4 4
6
'''


# 시간 초과
import sys 

lst = list()
for _ in range(int(sys.stdin.readline())):
    a, b = list(map(int, sys.stdin.readline().split())) 
    lst.append((a,b))
lst.sort(key = lambda x : (x[1], x[0]))    

i, j, cnt =0, 1, 1
while True:
    if lst[i][1] <= lst[j][0]:
        cnt += 1
        i = j
        j = i+1
    else:
        j += 1
    if i >= len(lst) or j >= len(lst):
        print(cnt)
        break
      
            
# # 시간 초과
# import sys 
# lst = list()

# for _ in range(int(sys.stdin.readline())):
#     a, b = list(map(int, sys.stdin.readline().split())) 
#     lst.append((a,b))
# lst.sort()
# print(lst)    
# i, j =0, 1
# count = 0
# start = 0
# while True:
#     cnt = 1
#     if i == len(lst)-1:
#         print(count)
#         exit(0)
#     while True:
#         print('1', i, j)
#         if lst[i][1] <= lst[j][0]:
#             print(i, j, lst[i], lst[j])
#             cnt += 1
#             i = j
#             j = i+1
#             print('2' , i, j)
#         else:
#             j += 1

#         if i >= len(lst) or j >= len(lst):
#             start+=1 
#             count = max(count, cnt)
#             i = start
#             j = i + 1
#             print('마지막 갱신된 ', i, j)
#             break

#     # count = max(count, cnt)
#     print('count : ' , count)        
            
