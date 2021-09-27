# 정답

# 퀴즈 - 팀의 이름 or 맴버의 이름 과 0또는 1의 숫자    0 -> 팀의 이름 , 1 -> 맴버의 이름
'''
N,M = map(int,input().split(' ')) # 입력받을 걸그룹 수 , 맞춰야 할 문제 수 

group,answer = list(), list() # 걸그룹 리스트, 정답

for _ in range(N): # 그룹명과 맴버명을 list에 저장
    group_name = input()
    total = int(input())
    for _ in range(total):
        member = input()
        group.append([group_name,member])

group.sort() # group 오름차순 정렬

for _ in range(M): # 퀴즈 코딩
    quiz = input()
    quiz_num = int(input())

    if quiz_num == 0: # 사전순으로 맴버의 이름 출력
        for i in group:
            if i[0] == quiz:
                # print(i[1])
                answer.append(i[1])
    elif quiz_num == 1: # 걸그룹 이름 출력
        for i in group:
            if i[1] == quiz:
                # print(i[0])
                answer.append(i[0])

for i in answer: # 정답 출력
    print(i);        

# group = [['twice', 'jihyo'],
#            ['twice', 'dahyeon'], 
#           ['twice', 'mina'], 
#           ['twice', 'momo'], 
#           ['twice', 'chaeyoung'],
#           ['twice', 'jeongyeon'], 
#           ['twice', 'tzuyu'],\
#            ['twice', 'sana'], 
#           ['twice', 'nayeon'],
#            ['blackpink', 'jisu'], 
#           ['blackpink', 'lisa'], 
#           ['blackpink', 'rose'], ['blackpink', 'jenny'], ['redvelvet', 'wendy'], ['redvelvet', 'irene'], ['redvelvet', 'seulgi'], ['redvelvet', 'yeri'], ['redvelvet', 'joy']]
# # print(group[1][0])

# # print(len(group))

# # print(len(group[1]))
# for i in group:
#     print(i[1])
'''
# 강사 코드

N,M = map(int,input().split(' ')) 

team_mem, mem_team = {}, {}

for i in range(N): 
    team_name, mem_num = input(), int(input())
    team_mem[team_name] = []
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):
    name, q = input(), int(input())
    if q:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)
