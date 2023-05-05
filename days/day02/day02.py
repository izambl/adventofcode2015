from pathlib import Path

input_path = Path(__file__).with_name('input')

with input_path.open('r', encoding='utf8') as input:
    lines = input.read()

boxes = [sorted([int(num) for num in box.split("x")]) for box in lines.split("\n")]

part01_total = 0
part02_total = 0
for box in boxes:
    a, b, c = box
    part01_total += 2 * a * b
    part01_total += 2 * a * c
    part01_total += 2 * b * c
    part01_total += min(a * b, a * c, b * c)

    part02_total += a + a + b + b
    part02_total += a * b * c

print(f"Part 01: {part01_total}")
print(f"Part 02: {part02_total}")
