import pyperclip
import re


def main():

    # TODO Find all the phone numbers and emails in the text
    # Regex pattern for finding phone numbers:
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # Area code
        (\s|-|\.)?                      # Seperator
        (\d{3})                           # First three digits
        (\s|-|\.)                       # Seperator
        (\d{4})                           # Last four digits
        (\s*(ext|x|ext.)\s*\d{2,5})?    # Extension
    )''', re.VERBOSE)

    # Regex pattern for matching email addresses:
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   # Username
        (@|\[at])                   # @ symbol 
        [a-zA-Z0-9.-]+      # Domain name
        (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE) # (|\sat\s|\s\[\sat\s]|\s\[at]\s|\(at\)|\s\(at\)\s|\s\(\sat\s\))

    text = str(pyperclip.paste())

    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[6] != "":
            phoneNum += ' x' + groups[6]
        matches.append(phoneNum)

    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print("No phone numbers or email addresses found.")


if __name__ == '__main__':
    main()
