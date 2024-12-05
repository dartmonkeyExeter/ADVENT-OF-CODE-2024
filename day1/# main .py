
# part one
list1 = []
list2 = []
ans = 0

with open('data.txt', 'r') as file:
    for line in file:
        list1.append(int(line.split('   ')[0]))
        list2.append(int(line.split('   ')[1]))

#list1.sort()
#list2.sort()

#for idx in range(0, len(list1)):
#    ans += abs(list1[idx] - list2[idx])
#

# part two

for i in list1:
    occurences = 0
    for j in list2:
        if i == j:
            occurences += 1

    ans += (occurences * i)

print(ans)