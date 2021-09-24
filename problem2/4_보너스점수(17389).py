# 맞았습니다! 
'''
N, S = int(input()), input();
#print(N, S)
bonus, grade = 0, 0

for i in range(N):
    # print(S[i])
    # print('grade : ' , grade)
    # print('bonus : ' , bonus)
    
    if S[i] == 'X':
        bonus = 0
        
    grade = grade + bonus

    if S[i] == 'O':
        bonus += 1
        grade += i+1
        
print(grade)

'''
# 강사 코드
N, S = input(), input()

score, bonus = 0, 0

for idx, OX in enumerate(S):
    if OX == 'O':
        score += idx+1+bonus
        bonus += 1
        # score, bonus = score + idx+1+bonus , bonus+1 코드의 간소화 

    else:
        bonus = 0

print(score)


    















"""

for idx, OX in enumerate(S):
    print(idx, OX);


결과값
0 X
1 O
2 O
3 O
4 X
5 O
6 O
7 X


"""