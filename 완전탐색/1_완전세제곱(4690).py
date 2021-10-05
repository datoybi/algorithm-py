# 맞았습니다!
a = 2

while a <= 100:
    for b in range(2, 100):
        for c in range(2, 100):
            for d in range(2, 100):
                if b <= c <= d:
                    if a**3 == b**3+c**3+d**3:
                        print("Cube = ",a,", Triple = (",b,",",c,",",d,")", sep="")
    a=a+1                    


#좋은 해답 - 대부분 나와 비슷하게 코딩함
for a in range(6,101):
    for b in range(2,101):
        for c in range(b+1,101):
            for d in range(c+1,101):
                if a**3 == b**3 + c**3 + d**3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
                if a**3 < b**3 + c**3 + d**3:
                    break