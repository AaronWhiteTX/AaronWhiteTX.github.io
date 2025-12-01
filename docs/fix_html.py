with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

fixes = [
    (76, '                <a\n'),
    (121, '                <a\n'),
    (128, '                <a\n'),
    (181, '                <a\n'),
    (188, '                <a\n'),
    (244, '                <a\n'),
    (299, '                <a\n'),
    (351, '                <a\n'),
    (394, '          <a\n'),
]

for line_num, text in reversed(fixes):
    lines.insert(line_num, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Fixed all 9 buttons")
