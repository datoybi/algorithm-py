'''
맞았습니다!
'''

while True:
    value = list(input().casefold())
    word = value[0]
    sentence = value[1:]
    count = 0

    if word == '#':
        exit(0)
    else :
        for i in sentence:
            if word == i:
                count+=1

        print(word , count)



