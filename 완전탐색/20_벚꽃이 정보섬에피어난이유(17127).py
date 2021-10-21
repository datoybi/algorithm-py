'''
첫째 줄에 벚나무의 개수 N이 주어진다. (4 ≤ N ≤ 10)
둘째 줄에 N개의 나무에 피어난 벚꽃의 개수 Ai가 순서대로 주어진다. (1 ≤ Ai ≤ 5)

7
2 5 3 1 4 2 3
67
2 + (5*3*1*4) + 2 + 3 = 67

5
1 1 2 1 1

5
4개로 묶음
'''
lst = [2, 5, 3, 1, 4, 2, 3]

for i in range(1, 5):
    for j in range(1, 5):
        for z in range(1, 5):
            print(i, j, z)
            print(lst[0:i], lst[i:j], lst[j:z], lst[z:-1])  
            
