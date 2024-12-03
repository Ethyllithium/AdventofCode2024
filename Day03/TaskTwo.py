total = 0

with open("input.txt", "r") as f:
    text = f.read()
do_mul = True
for i, char in enumerate(text):
    if text[i:i+4] == "mul(" and do_mul:
        first_term = ""
        second_term = ""
        after_comma = False
        for char2 in text[i+4:]:
            if char2.isdigit() and not after_comma:
                first_term += char2
            elif char2.isdigit() and after_comma:
                second_term += char2
            elif char2 == ",":
                after_comma = True
            elif char2 == ")" and first_term and second_term:
                print(first_term, second_term)
                print(int(first_term) * int(second_term))
                total += int(first_term) * int(second_term)
                break
            else:
                break
    elif text[i:i+4] == "do()":
        do_mul = True
    elif text[i:i+7] == "don't()":
        do_mul = False

print(total)
