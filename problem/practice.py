# arr = [ (21,'b'), (21,'a')]

arr = [(21,'Junkyu'), (21,'Dohyun'),(20,'Sunyoung')]
min = arr[0][0]

for i in arr:
    # min = arr[i][0]
    if min > arr[i][0]:
        min = arr[i][0]
    elif min == arr[i][0]:
        print(arr[i][0], ' ', arr[i][1])
    
    print()