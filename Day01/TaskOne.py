total = 0
left_side, right_side = [], []

with open("input.txt", "r") as f:
    for line in f:
        left_side.append(int(line.strip().split("   ")[0]))
        right_side.append(int(line.strip().split("   ")[1]))

left_side.sort()
right_side.sort()

for i in range(len(left_side)):
    total += abs(left_side[i] - right_side[i])

print(total)
