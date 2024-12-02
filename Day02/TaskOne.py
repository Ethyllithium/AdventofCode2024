total = 0

with open("input.txt", "r") as f:
    for line in f:

        safe = True
        numbers = [int(i) for i in line.strip().split(" ")]

        if not(numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)):
            safe = False
            continue

        for i in range(len(numbers)-1):
            if abs(int(numbers[i]) - int(numbers[i+1])) not in {1, 2, 3}:
                safe = False
                break

        if safe:
            total += 1

print(total)