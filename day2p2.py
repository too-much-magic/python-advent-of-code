safe = 0
def verify(nums):
    increasing = nums[0] < nums[1]
    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) > 3 or abs(nums[i] - nums[i + 1]) < 1 or (
                nums[i] < nums[i + 1]) != increasing:
            return False
    return True

with open("day2.txt") as file:
    for line in file:
        line_list = line.split()
        num_list = []
        for num in line_list:
            num_list.append(int(num))
        if verify(num_list):
            safe += 1
        else:
            for n in range(len(num_list)):
                temp = num_list.copy()
                del temp[n]
                if verify(temp):
                    safe += 1
                    break
print(safe)