'''
다음에 꼭 다시 풀어보기
4중포문은 쓰면 안되는듯 무조건 시간초과 난다
dp로 푸는 방법이 많은듯 한데 담에 봐보기
25 = 5*5 
26 = 5*5 + 1*1
11339 = 3
34567 = 4
15663 = 125 + 6 + 1 + 1 = 4
1 ≤ n ≤ 50,000

'''
# 시간초과 ㅠ
n = int(input())
count = 0
num = int(n**0.5) # 루트 구하는 공식임다 # 5
# num2 = int((n//4)**0.5)
# print(num2)
# result = [4]
result = 4 # 해당 되지 않을 시 ->4
# 시간초과 남

for i in range(int(n**0.5), 0, -1): # 25 -> 5 4 3 2 1 5 
    if i*i == n: 
        result = 1
        break
    else:
        tmp = n - i*i
        for j in range(int(tmp**0.5), 0, -1):
            if i*i+j*j == n:
                result = min(result, 2)
                continue
            else:
                tmp = n - i*i + j*j
                for z in range(int(tmp**0.5), 0, -1):
                    if i*i+j*j+z*z == n:
                        result = min(result, 3)
     

print(result)


# #남의 코드..  다음에 꼭 다시 풀어보기
# n = int(input())
# min_sum = 4 #최대는 4라고 증명되어있다, 아래 3중 for문에서 걸리지 않는다면 답은 4
# for a in range(int(n**0.5), int((n//4)**0.5), -1): #가능한 최소한의 범위로 축소해준다
#     if a*a == n:
#         min_sum = 1 #최소의 숫자일 경우
#         break   
#     else:
#         temp = n - a*a
#         for b in range(int(temp**0.5), int((temp//3)**0.5), -1): #남은 숫자는 3이니까 3으로 나누어줌
#             if a*a + b*b == n:
#                 min_sum = min(min_sum, 2)
#                 continue
#             else:
#                 temp = n - a*a - b*b
#                 for c in range(int(temp**0.5), int((temp//2)**0.5), -1):
#                     if n == a*a + b*b + c*c:
#                         min_sum = min(min_sum, 3)
                
# print(min_sum)


# 남의 코드다.. dp로 푼다고 하는데 나는 dp를 모른다.. 알때 한번 다시 봐야겠다.

# N = int(input())
# dp = [0,1]

# for i in range(2, N+1):
#     min_value = 1e9
#     j = 1

#     while (j**2) <= i:
#         min_value = min(min_value, dp[i - (j**2)])
#         j += 1

#     dp.append(min_value + 1)
# print(dp[N])


# n = int(input())
# # count = 0
# num = int(n**0.5) # 루트 구하는 공식임다
# original_n = n
# original_num = num

# while True:
#     count = 0
#     while True:
#         # print(num, n) # 5 30
#         if n == 1:
#             count+=1
#             print(count)
#             exit(0)
#         if num == 0: break
#         if n > 0:
#             if n - num**2 < 0: 
#                 num -= 1
#             else:
#                 count += 1
#                 # print('in : ' , num, num**2)
#                 n = n - num**2 # n = 1
#                 num -= 1 # num = 4
#         if n == 0:
#             print(count)
#             exit(0)
#         if n < 0:
#             break   
#         if count == 4: break
#     n = original_n
#     num = original_num-1
#     original_num -= 1        


