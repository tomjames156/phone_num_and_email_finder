# import pyperclip module and regex module
import re
import pyperclip

# store the text from the clipboard in a variable 
clipboard_text = pyperclip.paste()

# create a variable for the results
results_str = ""
# create a phone number regex with groups

phone_regex = re.compile(r'''
(\+234|0)?    # country code or starting zero
(\s)?    # separator
(\d{3})    # first three digits 
(\s)?    # separator
(\d{3})    # second three digits
(\s)?    # separator
(\d{4})    # last four digits
''', re.VERBOSE)

# create an email regex with groups
# join each group together before adding it to the results variable
# copy the text back to the clipboard
print(phone_regex.search("0706 829 3037").group())