'''
맞았습니다!
'''
def multiply(lst) :
    result = 1
    for i in range(0, len(lst)):
        result = lst[i] * result
    return result

N, lst = input(), list(map(int, input().split()))
max = 0

for i in range(1, len(lst)):
    for j in range(i+1, len(lst)):
        for z in range(j+1, len(lst)):
            if lst[0:i] and lst[i:j] and lst[j:z] and lst[z:] :
                # print(i, j, z)
                # print(lst[0:i], lst[i:j], lst[j:z], lst[z:])  
                sum = multiply(lst[0:i]) + multiply(lst[i:j]) + multiply(lst[j:z]) + multiply(lst[z:])
                if max < sum :
                    max = sum

print(max)
