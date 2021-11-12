'''
len(A) <= len(B)
A의 길이가 B와 같아질 때까지 A의 앞이나 뒤에 아무 알파벳 추가 
A.B차이를 최소로 하는 프로그램 작성

azc xyabcxy
1
abc xxbzzz
2


'''
# 1차 시도 : 잎이랑 뒤에 넣는것만 고려했다..
# # A, B ='adaabc', 'aababbc'
# A, B = input().split()
# count = 0

# if len(A) == len(B): # 길이가 같으면 판별
#     for i in range(len(B)):
#         if A[i] != B[i] :
#             count += 1
#     print(count)
#     exit(0)

# elif len(A) != len(B): # 길이가 다를때 A 앞이나 뒤에 추가
#     if A in B : # B안에 A가 있으면 0
#         print('0')
#         exit(0)
#     else: 
#         dif = len(B) - len(A)
#         front, back = B[0:dif], B[-dif:]
#         front_a, back_a = front+A , A+back
#         middle_a = ''

#         if dif % 2 == 0:
#             # m_dif = dif/2
#             # print(int(dif/2))
#             middle_a = B[0:int(dif/2)] + A + B[int(-dif/2):]

#         print(front_a, back_a, middle_a)

#         front_count, back_count, middle_count = 0, 0, len(B)
#         if dif % 2 == 0:
#             middle_count = 0

#         for i in range(len(B)):
#             if front_a[i] != B[i] :
#                 front_count += 1
#             if back_a[i] != B[i] :
#                 back_count += 1
#             if dif % 2 == 0:
#                 if middle_a[i] != B[i] :
#                     middle_count += 1
                    

# print(min(front_count,back_count,middle_count))


# 2차시도 : 앞 뒤 뿐만 아니라 중간에 배치하는 것도 고려
# A, B ='abc', 'xxbzzz'
A, B = input().split()
count = 0

if len(A) == len(B): # 길이가 같으면 판별
    for i in range(len(B)):
        if A[i] != B[i] :
            count += 1
    print(count)
    exit(0)

elif len(A) != len(B): # 길이가 다를때 A 앞이나 뒤에 추가
    if A in B : # B안에 A가 있으면 0
        print('0')
        exit(0)
    else: 
        dif = len(B) - len(A)

        for j in range(dif+1):
            print(dif - j, j)
            front, back = B[0:dif-j], B[-j:]
            print(front, back)
            # front_a, back_a = front+A , A+back


#         front, back = B[0:dif], B[-dif:]
#         front_a, back_a = front+A , A+back
#         middle_a = ''

#         if dif % 2 == 0:
#             # m_dif = dif/2
#             # print(int(dif/2))
#             middle_a = B[0:int(dif/2)] + A + B[int(-dif/2):]

#         print(front_a, back_a, middle_a)

#         front_count, back_count, middle_count = 0, 0, len(B)
#         if dif % 2 == 0:
#             middle_count = 0

#         for i in range(len(B)):
#             if front_a[i] != B[i] :
#                 front_count += 1
#             if back_a[i] != B[i] :
#                 back_count += 1
#             if dif % 2 == 0:
#                 if middle_a[i] != B[i] :
#                     middle_count += 1
                    

# print(min(front_count,back_count,middle_count))

