# 절반을 오른쪽으로 전달, 홀수개 + 1 -> 1순환 
# 처음 홀수개 -> 보충먼저, 순환수 x

# 테스트 케이스 T
# 인원 N
# 사탕개수 C
 
 # 모르겠어서 강사 코드 봄

def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1 
    # set은 중복을 제거해주는데 set의 길이가 1이라는 것은 모든 수가 같다는 의미

def teacher(N, candy):
    tmp_lst = [0 for i in range(N)]
    for idx in range(N):
        if candy[idx] % 2: # 2로 나눴는데 나머지가 있으면 
            candy[idx] += 1
        candy[idx] //= 2
        tmp_lst[(idx + 1) % N] = candy[idx] // 2

    for idx in range(N):
        candy[idx] += tmp_lst[idx]

    return candy

def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0

    while not check(N, candy): # 모든 수가 같지 않으면 실행
        cnt += 1
        candy = teacher(N, candy)
    print(cnt)

for i in range(int(input())): # 입력받는 값 수만큼 process 함수 실행
    process()

