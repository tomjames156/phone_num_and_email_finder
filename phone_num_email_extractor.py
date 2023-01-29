# import pyperclip module and regex module
import re, pyperclip

# store the text from the clipboard in a variable 
clipboard_text = pyperclip.paste().split()

# create a variable for the results
results_str = ""

# create a phone number regex with groups
phone_regex = re.compile(r'''
^(\+243|0)+    # country code or starting zero
(\s)?    # separator
(\d{3})    # first three digits 
(\s)?    # separator
(\d{3})    # second three digits
(\s)?    # separator
(\d{4})$    # last four digits
''', re.VERBOSE)

# create an email regex with groups
email_regex = re.compile(r'''
^([a-zA-Z0-9]+[_\.-]*[a-zA-Z0-9]+)    # email name
(@)    # at symbol
([\w\-]+)    # email provider
(\.)    # dot separator
([\w\-\.]+)$    # domain extension
''', re.VERBOSE)

def is_match(text):
    """Checks if a text is a phone number or an email"""
    phone_number = phone_regex.search(text)
    email = email_regex.search(text)

    if((phone_number == None) and (email == None)):
        return False
    else:
        return True

# adds the text to results if it is a match
for text in clipboard_text:
    if(is_match(text)):
        results_str += f"{text}\n"

results_str = results_str.strip()

# copy the text back to the clipboard
pyperclip.copy(results_str)