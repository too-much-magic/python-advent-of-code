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

intervals = [[0, 0]]
spaces = None
for n in range(1, len(ids)):
    if ids[n] == '.':
        if not spaces:
            spaces = [[n, n]]
        elif ids[n] == ids[n - 1]:
            spaces[len(spaces) - 1][1] += 1
        else:
            spaces.append([n, n])
    elif ids[n] == ids[n - 1]:
        intervals[len(intervals) - 1][1] += 1
    else:
        intervals.append([n, n])

intervals.sort(reverse=True)
for interval in intervals:
    for space in spaces:
        diff = (space[1] - space[0]) - (interval[1] - interval[0])
        if diff >= 0 and space[0] < interval[0]:
            ids[interval[0]:interval[1] + 1], ids[space[0]:space[1] - diff + 1] = \
                ids[space[0]:space[1] - diff + 1], ids[interval[0]:interval[1] + 1]
            space[0] += (interval[1] - interval[0]) + 1
            break

checksum = 0
for index, value in enumerate(ids):
    if value == ".":
        continue
    checksum += (index * value)
print(checksum)
