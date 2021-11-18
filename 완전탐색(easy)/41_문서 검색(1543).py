'''
맞았습니다!!

'''
santance, word = list(input()), list(input())
count = 0 
# print(santance, word)

while True:
    # print(santance)
    if len(santance) < len(word): # word 길이가 santance보다 길면 break
        break
    if word == santance[0:len(word)]: # word 가 같으면 count 올리고 word 삭제
        count += 1
        del santance[0:len(word)]
    else: # word가 같지 않으면 santance 하나씩 삭제
        del santance[0] 
    
    
print(count)