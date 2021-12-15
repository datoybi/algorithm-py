left, right = input().split()
strings = list(input())

keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
mo = 'yuiophjklbnm'

xl, yl, xr, yr = None, None, None, None

for i in range(len(keyboard)):
    if left in keyboard[i]:
        xl = i
        yl = keyboard[i].index(left)

    if right in keyboard[i]:
        xr = i
        yr = keyboard[i].index(right)

time = 0
for string in strings:
    time += 1
    if string in mo:
        for i in range(len(keyboard)):
            if string in keyboard[i]:
                nx = i
                ny = keyboard[i].index(string)

                time += abs(nx - xr) + abs(ny - yr)
                xr = nx
                yr = ny
                break
    else:
        for i in range(len(keyboard)):
            if string in keyboard[i]:
                nx = i
                ny = keyboard[i].index(string)

                time += abs(nx - xl) + abs(ny - yl)
                xl = nx
                yl = ny
                break

print(time)