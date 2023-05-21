chapterNumber = input(
    "Enter the name of the Echopraxia-Chapter-# without the .md: ")
chapterNumber = str(chapterNumber)
with open('Echopraxia-Chapter-' + chapterNumber + '.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()


new_lines = []
previous_line = ''

for line in lines:
    if line.startswith('[[Echopraxia-Chapter'):
        new_lines.append(previous_line)
    new_lines.append(line)
    previous_line = line if line.strip() else previous_line

with open('Echopraxia-Chapter-' + chapterNumber + '.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
