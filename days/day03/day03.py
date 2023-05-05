from pathlib import Path

input_path = Path(__file__).with_name('input')

with input_path.open('r', encoding='utf8') as input:
    lines = input.read()



x = 0
y = 0
houses = { "0-0": 1}
for instruction in list(lines):
    match instruction:
        case "<":
            x -= 1
        case ">":
            x += 1
        case "^":
            y += 1
        case "v":
            y -= 1
    house = f"{x}-{y}"
    if house in houses:
        houses[house] += 1
    else:
        houses[house] = 1

print(f'Part01: {len(houses)}')


instructions = list(lines)
x_a = 0
y_a = 0
x_b = 0
y_b = 0
houses2 = { "0-0": 1}
for i in range(0, len(instructions), 2):
    ins_a = instructions[i]
    ins_b = instructions[i + 1]
    match ins_a:
        case "<":
            x_a -= 1
        case ">":
            x_a += 1
        case "^":
            y_a += 1
        case "v":
            y_a -= 1
    match ins_b:
        case "<":
            x_b -= 1
        case ">":
            x_b += 1
        case "^":
            y_b += 1
        case "v":
            y_b -= 1

    house_a = f"{x_a}-{y_a}"
    house_b = f"{x_b}-{y_b}"

    if house_a in houses2:
        houses2[house_a] += 1
    else:
        houses2[house_a] = 1

    if house_b in houses2:
        houses2[house_b] += 1
    else:
        houses2[house_b] = 1

print(f'Part02: {len(houses2)}')