"""
    두베까지 풀어보고 풀면 잘 풀었다! 30분안에 못풀었으면 해설 들으며 강의 듣고 
    다시 혼자 풀어보기
    
    제목 : 음계 
    난이도 : 하
    유형 : 배열, 구현
    추천 풀이 시간 : 15분 
    (못품ㅠ)
    python3나 pypy3로 체점하기 

    느낀점 : 그냥 문제만 맞춰도 ㄱㅊ하나보다 다장조라 dictionary 만들지 않아도 말이다.
    https://github.com/ndb796/Fast_Campus_Algorithm_Lecture_Notes
"""


# a = input()
# array = ['1','2','3','4','5','6','7','8']

# dict = {
#     'c':'1',
#     'd':'2',
#     'e':'3',
#     'f':'4',
#     'g':'5',
#     'a':'6',
#     'b':'7',
#     'C':'8',
# }

# flag = True;
# rflag = True;

# for i in range(0, len(dict)):
#     print(dict[i]);

#     if(a[i] != array[i]):
#         flag = False;

# reversedArray = list(reversed(array));

# for i in range(0, len(reversedArray)):
#     if(a[i] != array[i]):
#         rflag = False;


# if flag == True:
#     print("ascending")
# elif rflag == True:
#     print("descending")
# else:
#     print("mixed")


# 해답
arr = input().split(' ')
arr = list(map(int, arr))

descending = True
ascending = True

for i in range(1,8) :
    if arr[i] > arr[i-1]:
        descending = False
    elif arr[i] < arr[i-1]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")

# 두번째 시도 
num = list(map(int, input().split(' ')))
answer = [1,2,3,4,5,6,7,8]
r_answer = list(reversed(answer))

if num == answer:
    print('ascending')
elif num == r_answer:
    print('descending')
else:
    print('mixed')


