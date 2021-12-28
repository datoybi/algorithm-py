'''
선끼리 교차하지 않기
각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면, 
그 단어는 '좋은 단어'이다.


'''
import sys
count = 0
for _ in range(int(sys.stdin.readline())):
    # word = list(sys.stdin.readline().rstrip())
    j = 0
    if word.count('A') % 2 == 0 or word.count('B') % 2 == 0: # 두개의 수가 홀수면    
        for i in range(10):
            if len(word) <= 1: 
                break
            if j == len(word)-1:
                j = 0
            print(word[j:j+2])
            if word[j:j+2] == 'AA' or word[j:j+2] == 'BB':
                del word[j:j+1]
                j = 0
            
