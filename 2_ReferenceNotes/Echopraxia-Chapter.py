chapterNumber = input(
    "Enter the name of the Echopraxia-Chapter-# without the .md: ")
chapterNumber = str(chapterNumber)

with open('Echopraxia-Chapter-' + chapterNumber + '.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

lines = [line for line in lines if line.strip()]  # This line removes all blank lines

new_lines = []
previous_line = None

for line in lines:
    if line.startswith('[[Echopraxia-Chapter'):
        if previous_line is not None and previous_line.strip() != '':
            new_lines.append('\n')
    new_lines.append(line)
    previous_line = line

with open('Echopraxia-Chapter-' + chapterNumber + '.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
