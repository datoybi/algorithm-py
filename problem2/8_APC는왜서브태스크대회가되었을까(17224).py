# 쉬운 버전의 난이도 sub1, 어려운 버전의 난이도 sub2 
# 결과물은 나오는데 오답이라고 뜸
'''
N, L, K = map(int, input().split())  # 문제의 개수 N, 역량 L, 최대 개수 K
quiz, score, count = list(), 0, 0

for i in range(N): # 퀴즈 등록
    if count == L:
        break
    sub1, sub2 =  map(int, input().split())
    if sub1 <= L and sub2 <= L:
        score += 140
        count+=1
    else:
        quiz.append((sub1, sub2))

for j in range(0, K-count):
    if quiz[j][0] <= L  and quiz[j][1] > L:
        # print( quiz[j][0],  quiz[j][1])
        score += 100
    
print(score)
'''

# 강사 답
N, L, K = map(int, input().split()) 
easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L: # 풀 수 있는 어려운 문제 수 카운트
        hard += 1
    elif sub1 <= L: # 풀 수 있는 쉬운 문제 수 카운트
        easy += 1

#hard 문제
ans = min(hard, K) * 140

# easy 
if hard < K:
    ans += min(K-hard, easy) * 100

print(ans)

