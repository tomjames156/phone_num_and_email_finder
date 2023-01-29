# import pyperclip module and regex module
import re, pyperclip

# store the text from the clipboard in a variable 
clipboard_text = pyperclip.paste()

# create a variable for the results
results_str = ""

# create a phone number regex with groups
phone_regex = re.compile(r'''
(\+243|0)+    # country code or starting zero
(\s)?    # separator
(\d{3})    # first three digits 
(\s)?    # separator
(\d{3})    # second three digits
(\s)?    # separator
(\d{4})    # last four digits
''', re.VERBOSE)

# create an email regex with groups
email_regex = re.compile(r'''
([a-zA-Z0-9]+[_\.-]*[a-zA-Z0-9]+)    # email name
(@)    # at symbol
([\w\-]+)    # email provider
(\.)    # dot separator
([\w\-\.]+)    # domain extension
''', re.VERBOSE)

# find all email and phone number matches
emails = email_regex.findall(clipboard_text)
phone_nos = phone_regex.findall(clipboard_text)
all_matches = emails + phone_nos

# rejoin each group to a string
for match_tuple in all_matches:
    current_match = ""
    for match_group in match_tuple:
        current_match += match_group
    results_str += f"{current_match}\n"

if(len(results_str) > 0):
    # copy the text back to the clipboard
    pyperclip.copy(results_str)
    print("Copied to Clipboard!")
else:
    print("No phone numbers or email addresses found😢")