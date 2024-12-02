def spacing(values):
    for i in range(len(values) - 1):
        if abs(int(values[i]) - int(values[i + 1])) not in {1, 2, 3}:
            return False
    return True


def ordered(values):
    if not (values == sorted(values) or values == sorted(values, reverse=True)):
        return False
    return True


total = 0

with open("input.txt", "r") as f:
    for line in f:
        numbers = [int(i) for i in line.strip().split(" ")]

        if ordered(numbers) and spacing(numbers):
            total += 1

        else:
            for i in range(len(numbers)):
                sublist = list(numbers)
                del sublist[i]
                if ordered(sublist) and spacing(sublist):
                    total += 1
                    break

print(total)

