import pyperclip
import re


def main():
    # TODO Get the text off of the clipboard
        # TODO Use pyperclip to copy and paste information from clipboard

    # TODO Find all the phone numbers and emails in the text
    # Regex pattern for finding phone numbers:
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # Area code
        (\s|-|\.)?                      # Seperator
        \d{3}                           # First three digits
        (\s|-|\.)                       # Seperator
        \d{4}                           # Last four digits
        (\s*(ext|x|ext.)\s*\d{2,5})?    # Extension
    )''', re.VERBOSE)

    # Regex pattern for matching email addresses:
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   # Username
        (@|at)              # @ symbol 
        [a-zA-Z0-9.-]+      # Domain name
        (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE) # (|\[at]|\s\[\sat\s]|\s\[at]\s|\(at\)|\s\(at\)\s|\s\(\sat\s\))

        # TODO Find all (not just first) matches of above regexes
        # TODO Neatly format found information into a single string

    # TODO Paste the found information onto the clipboard
        # TODO Provide message for if information was found or not
        # TODO Paste information to clipboard


if __name__ == '__main__':
    main()
