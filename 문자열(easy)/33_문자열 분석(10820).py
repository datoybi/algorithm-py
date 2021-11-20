# 맞았습니다!

while True:
    try:
        sentence =  input()
        lower, upper, number, blank = 0, 0, 0, 0

        for i in sentence:
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            elif i.isnumeric():
                number += 1
            elif i == ' ':
                blank += 1
        print(lower, upper, number, blank)
        
    except:
        exit(0)
