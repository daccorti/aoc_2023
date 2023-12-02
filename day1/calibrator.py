import re

f= open("part_a.txt", "r")
contents = f.readlines()

data = [line.strip("\n") for line in contents]
vals =[]
for i in range(len(data)):
    nums = re.sub("[^0-9]", "",data[i])
    if len(nums) < 2:
        x = nums[0]
        y = nums[0]
    else:
        x = nums[0]
        y = nums[-1]
    pr = x+y
    vals.append(pr)

answer = sum([int(i) for i in vals])

print(answer)