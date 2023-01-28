# import pyperclip module and regex module
import re
import pyperclip

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
([a-z]+\w+)    # email name
(@)    # at symbol
([a-z]+)    # email provider
(\.com|\.me)    # domain extension
''', re.VERBOSE)

# join each group together before adding it to the results variable
# copy the text back to the clipboard
print(phone_regex.findall("+2437166293027 08155807084 08038672593"))
emails = email_regex.findall('gbae67@gmail.comtomi134@protonmail.com rosettadiamond@yahoo.com+2437068293037')
# print(emails)