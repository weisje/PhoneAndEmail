import pyperclip
import re


def main():
    # TODO Get the text off of the clipboard
        # TODO Use pyperclip to copy and paste information from clipboard

    # TODO Find all the phone numbers and emails in the text
        # Regex pattern for finding phone numbers:
        phoneNumber = re.compile(r'''(
            (\d{3}|\(\d{3}\))?              # Area code
            (\s|-|\.)?                      # Seperator
            \d{3}                           # First three digits
            (\s|-|\.)                       # Seperator
            \d{4}                           # Last four digits
            (\s*(ext|x|ext.)\s*\d{2,5})?    # Extension
        )''', re.VERBOSE)

        # TODO Create a regex for matching email addresses
        # TODO Find all (not just first) matches of above regexes
        # TODO Neatly format found information into a single string

    # TODO Paste the found information onto the clipboard
        # TODO Provide message for if information was found or not
        # TODO Paste information to clipboard


if __name__ == '__main__':
    main()
