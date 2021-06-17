def bubblesort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


import random

data_list = random.sample(range(100), 50)

print(data_list)
print("-----------------------------")
print(bubblesort(data_list))
