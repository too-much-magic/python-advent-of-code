with open("day9.txt") as file:
    disk = [int(i) for i in file.readline().rstrip()]

ids = []

for index, num in enumerate(disk):
    if index % 2 == 0:
        for n in range(num):
            ids.append(index // 2)
    else:
        for n in range(num):
            ids.append(".")

p1, p2 = 0, len(ids) - 1

while p1 < p2:
    if type(ids[p1]) == int:
        p1 += 1
    elif type(ids[p2]) == str:
        p2 -= 1
    else:
        ids[p1], ids[p2] = ids[p2], ids[p1]

checksum = 0
for index, value in enumerate(ids):
    if value == ".":
        break
    checksum += (index * value)
print(checksum)
