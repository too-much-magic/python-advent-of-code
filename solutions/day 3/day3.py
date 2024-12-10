with open("day3.txt", 'r') as file:
    mult_sum = 0
    for line in file:
        for n in range(len(line)):
            if line[n:n + 4] == "mul(":
                head = n + 4
                mode = 1
                num1, num2 = "", ""
                while head < len(line):
                    if line[head] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ','):
                        break
                    elif line[head] == ',':
                        mode = 2
                    elif mode == 1:
                        num1 += line[head]
                    elif mode == 2:
                        num2 += line[head]
                    head += 1
                if line[head] != ')':
                    head += 1
                else:
                    if num1 != "" and num2 != "":
                        mult_sum += int(num1) * int(num2)
                        print(num1, num2)
    print(mult_sum)
