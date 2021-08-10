'''
    제목 : 문서검색
    난이도 : 하
    유형 : 탐색
    시간 : 20분

'''

sentence = 'ababababa'
str = 'aba'
n = 0 


# print(sentence[:len(str)])
# sentence = sentence.removeprefix(str);
# print(sentence)

while(sentence):
     if str == sentence[:len(str)]:
        n += 1
        sentence = sentence.removeprefix(str);
        print(sentence)
     else:
        sentence.replace(sentence[0], '', 1)
        print(sentence)
        