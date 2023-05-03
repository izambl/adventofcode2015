from pathlib import Path

input_path = Path(__file__).with_name('input')

with input_path.open('r', encoding='utf8') as input:
    lines = input.read()

floor01 = 0
basement = None

for position, instuction in enumerate(lines):
    if instuction == '(':
        floor01 += 1
    if instuction == ')':
        floor01 -= 1
    if floor01 < 0 and basement is None:
        basement = position

print(f'Part01: {floor01}')
print(f'Part02: {basement + 1}')
