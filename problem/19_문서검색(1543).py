'''
    제목 : 문서검색
    난이도 : 하
    유형 : 탐색
    시간 : 20분
    런타임 에러시 : https://www.secmem.org/blog/2020/09/19/rte/
'''
# pypy3은 런타임 에러, pyhton3은 맞음... 무슨 차이 일까

# sentence = input()
# str = input()
# n = 0 

# while(sentence):
#      if str == sentence[:len(str)]:
#         n += 1
#         sentence = sentence.removeprefix(str);
#       #   print(sentence)
#      else:
#         sentence = sentence.replace(sentence[0], '', 1)
#       #   print(sentence)
        

# print(n)


#해답
'''
   문제풀이 핵심 아이디어 
   문서의 길이는 최대 2,500이고 단어의 길이는 최대 50입니다.
   단순히 모든 경우의 수를 계산하여 문제를 해결 할 수 있습니다.
   시간 복잡도 O(NM)의 알고리즘으로 해결할 수 있습니다.
'''

