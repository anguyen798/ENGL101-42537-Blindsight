import pyperclip

string = input("Type the string here without quotes: ")
def string_replace(string):
    charactersRemove = ['*', '\\', '/', '<', '>', ':', '|', '?']
    for char in charactersRemove:
        string = string.replace(char, '')  # updating string after each replacement
    string = string.replace(' ', '-')
    pyperclip.copy(string)  # copy the formatted string to clipboard

string_replace(string)