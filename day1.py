list1 = []
list2 = []

with open("day1.txt") as file:
    for line in file:
        curr = line.split()
        list1.append(int(curr[0]))
        list2.append(int(curr[1]))

list1.sort()
list2.sort()

dist = 0

for n in range(len(list1)):
    dist += abs(list1[n] - list2[n])
    
print(dist)
