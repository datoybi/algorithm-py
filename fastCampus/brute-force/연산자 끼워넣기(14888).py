'''
핵심
int 범위: -21억 ~ 21억 -> int형 변수를 쓰면 된다!!

시간복잡도
10! = 362880 

N-1개의 카드 중에서 중복없이(같은 카드는 한번 사용해서) N-1개를 순서있게 나열하기
어렵다 어려워...!!!!! 꼭 다시 풀어보기...

'''
import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
min = 1e9
max = -1e9
print(nums)
print(operator)


def calculator(operand1, operator, operand2):
    if operator == 0:
        return operand1 + operand2
    if operator == 1:
        return operand1 - operand2
    if operator == 2:
        return operand1 * operand2
    if operator == 3:
        if operand1 < 0:
            return - ((-operand1) // operand2)
        else:
            return operand1 // operand2


def rec_func(k, value):
    # print('k : ', k, ' , value : ', value)
    if k == n - 1:
        global min, max
        min = min if min < value else value
        max = max if max > value else value
    else:
        global operator
        for cand in range(4):
            if operator[cand] >= 1:
                operator[cand] -= 1
                rec_func(k + 1, calculator(value, cand, nums[k + 1]))
                operator[cand] += 1


rec_func(0, nums[0])
print(max)
print(min)

'''
n = 3
num = [3, 4, 5]
operator = [1, 0, 1, 0]

i) rec_func(0, 3)
rec_func(0, 3)
	k = 0, value = 3
	cand = 0
	operator[0] = 0
	rec_func(1, calculator(3, 0, nums[1]) // 3, 0, 4
		rec_func(1, 7)
			k = 1, value = 7
			cand = 2
			operator[2] = 0
				rec_func(2, calculator(7, 2, nums[2]) // 7, 2, 5
				rec_func(2, 35)
					k = 3, value = 35
						k == n-1 : max = 35
			opertaor[2] = 1
	operator[0] = 1
	k = 0, value = 3 operator[2] = 0
	rec_func(1, calculator(3, 2, nums[1]) // 3, 2, 4
	rec_func(1, 12)
		k = 1, value = 12
		operator[0] = 0
		rec_func(2, calculator(12, 0, num[2]) // 12, 0, 5
		rec_func(2, 17)
			min = 17

'''
