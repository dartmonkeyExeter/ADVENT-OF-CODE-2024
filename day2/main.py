import copy

list1 = []
safe = 0
prev = 0

with open('C:/Users/aaronhampson/Downloads/at first i was afraid/day2/data.txt', 'r') as file:
    line_count = int(len(file.readlines())) - 1

with open('C:/Users/aaronhampson/Downloads/at first i was afraid/day2/data.txt', 'r') as file:
    for idx, line in enumerate(file):
        list1.append(line.split(' '))
        if idx != line_count:
            list1[-1][-1] = list1[-1][-1].split("\n")[0]


for idx, i in enumerate(list1):
    for jdx, j in enumerate(i):
        list1[idx][jdx] = int(list1[idx][jdx])

asc_or_desc_test = 0

for idx, i in enumerate(list1):
    is_safe = True

    asc = copy.deepcopy(i)
    desc = copy.deepcopy(i)

    asc.sort()
    desc.sort(reverse=True)

    if i != asc:
        is_safe = False

    if is_safe:
        for jdx, j in enumerate(i):
            if jdx == 0:
                prev = j
                continue
            elif abs(prev - j) > 3 or abs(prev - j) == 0:
                is_safe = False
                break
        
    if is_safe:
        safe += 1

print(safe)