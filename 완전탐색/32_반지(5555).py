'''
맞았습니다!
'''
str, N = input(), int(input())
count = 0
str_lst = list()

for i in range(N):
    str_lst.append(input()) # 초기값 세팅

for item in str_lst : # str list 만큼 요소 뽑아오기
    for i in range(0, len(item)+1):
        tmp = item
        j = i + len(str)

        if j <= len(item): # j가 LENGTH보다 작을 때        
            if tmp[i:j] == str:
                count += 1
                break

        elif j > len(tmp): # j가 length를 초과했다면   
            s = j-len(tmp)
    
            if tmp[i:j]+tmp[0:s] == str: # 덧붙이기
                count += 1
                break

print(count)