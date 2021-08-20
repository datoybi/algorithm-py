arr = []
ordered_list = []
n = int(input())
index = 0

for i in range(n):
    arr.append(int(input()))
    ordered_list.append(i+1)

print(arr)
print(ordered_list)

while(ordered_list):

    if arr[0] != ordered_list[index]:
        print('+')
        index+=1
        
    elif arr[0] == ordered_list[index]:
        print('+')
        print('-')
        del arr[0]
        del ordered_list[index];
        index-=1
