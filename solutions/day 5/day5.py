from collections import defaultdict

with open("day5.txt") as file:
    rules = []
    order = []

    for line in file:
        line = line.rstrip()
        if line == "":
            break
        rules.append(line.split("|"))
    for line in file:
        line = line.rstrip()
        order.append(line.split(","))

    for rule in rules:
        rule[0] = int(rule[0])
        rule[1] = int(rule[1])

    for update in order:
        for i in range(len(update)):
            update[i] = int(update[i])

    rules_dict = defaultdict(set)

    for rule in rules:
        rules_dict[rule[0]].add(rule[1])

    page_sum = 0
    for update in order:
        valid = True
        seen = set()
        for page in update:
            for rule in seen:
                if rule in rules_dict[page]:
                    valid = False
                    break
            seen.add(page)
        if valid:
            page_sum += update[len(update) // 2]

    print(page_sum)