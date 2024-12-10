def verify_mul(segment, i):
    if segment[i:i + 4] == "mul(":
        head = i + 4
        mode = 1
        num1, num2 = "", ""
        while head < len(segment):
            if segment[head] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ','):
                break
            elif segment[head] == ',':
                mode = 2
            elif mode == 1:
                num1 += segment[head]
            elif mode == 2:
                num2 += segment[head]
            head += 1
        if head < len(segment) - 1 and segment[head] != ')':
            return 0
        else:
            if num1 != "" and num2 != "":
                return int(num1) * int(num2)
    return 0


with open("day3.txt", 'r') as file:
    mult_sum = 0
    do = True
    for line in file:
        for n in range(len(line)):
            if do:
                mult_sum += verify_mul(line, n)
            if line[n:n + 4] == "do()":
                do = True
            elif line[n:n + 7] == "don't()":
                do = False
    print(mult_sum)
