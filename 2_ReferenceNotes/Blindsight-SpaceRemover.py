import re

def remove_redundant_spacing(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # The regular expression matches a newline character that is not preceded 
    # or followed by another newline character. This will only match newlines
    # that are within a paragraph, leaving the newlines between paragraphs and 
    # the newlines around the chapter markers untouched.
    pattern = r"(?<!\n)\n(?!\n)"
    cleaned_content = re.sub(pattern, " ", content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

filename = input("Enter the chapter without the .md: ")
remove_redundant_spacing('Echopraxia-Chapter-' + filename + '.md')
