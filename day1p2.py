from collections import defaultdict

list1 = []
list2 = []

with open("day1.txt") as file:
    for line in file:
        curr = line.split()
        list1.append(int(curr[0]))
        list2.append(int(curr[1]))
    
freq = defaultdict(int)

for num in list2:
    freq[num] += 1
    
sim_score = 0
for num in list1:
    sim_score += (freq[num] * num)
    
print(sim_score)