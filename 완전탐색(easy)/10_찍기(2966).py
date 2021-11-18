'''
맞았습니다!
'''
N, answer = int(input()), list(input())

Adrian, Bruno, Goran= ['A','B','C'], ['B', 'A', 'B', 'C'], ['C', 'C', 'A', 'A','B','B']
result = {
    'Adrian': 0,
    'Bruno' : 0,
    'Goran' : 0
}

for i in range(0,len(answer)):
    if answer[i] == Adrian[i%len(Adrian)]:
        result['Adrian'] +=1
    if answer[i] == Bruno[i%len(Bruno)]:
        result['Bruno'] +=1
    if answer[i] == Goran[i%len(Goran)]:
        result['Goran'] +=1

print(max(result.values()))
for key, value in result.items():
    if value == max(result.values()):
        print(key)