import collections

total = 0
left_side, right_side = [], []

with open("input.txt", "r") as f:
    for line in f:
        left_side.append(int(line.strip().split("   ")[0]))
        right_side.append(int(line.strip().split("   ")[1]))

right_side_dict = collections.Counter(right_side)
for number in left_side:
    total += right_side_dict[number]*number

print(total)
