import sys

# 입력 받을 개수
n = int(sys.stdin.readline())

# 값 입력받기
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

# 결과 변수 및 이미 한 번 체크하였었던 수인지를 확인하기 위한 리스트 선언
result = 0
already = [0] * 1000001 # 0으로 다 채운 list

# print(already)

# 확인 진행
for i in data:
    # print(already[i]) # 0 이나 1
    if already[i]: 
        continue
    already[i] = 1 # 반복하지 않기위해 사용
    cur = data[0] # 2
    cnt = 1
    for j in range(1 ,len(data)):
        if i == data[j]: # i(삭제할 숫자)랑 data[j] 같으면 continue
            continue
        if cur == data[j]: # cur이랑 같으면 +1
            cnt += 1
        else: # 다르면 cnt = 1
            cur = data[j]
            cnt = 1
        result = max(result, cnt)

print(result)