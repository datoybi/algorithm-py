
data_list = [(10,10),(15,12),(20,10),(25,8),(30,5)]

def calculate(data_list, capacity):
    data_list = sorted(data_list, key=lambda x:x[1]/x[0], reverse=True)
    total = 0
    details = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total, details

print(calculate(data_list, 30))
