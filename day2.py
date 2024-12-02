safe = 0
with open("day2.txt") as file:
    for line in file:
        line_list = line.split()
        nums = []
        for num in line_list:
            nums.append(int(num))
        increasing = nums[0] < nums[1]
        for n in range(len(nums) - 1):
            if abs(nums[n] - nums[n + 1]) > 3 or abs(nums[n] - nums[n + 1]) < 1 or (
                    nums[n] < nums[n + 1]) != increasing:
                break
        else:
            safe += 1
print(safe)
