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
([a-zA-Z0-9]+[_\.-]*[a-zA-Z0-9]+)    # email name
(@)    # at symbol
([\w\-]+)    # email provider
(\.)    # dot separator
([\w\-\.]+)    # domain extension
''', re.VERBOSE)

# copy the text back to the clipboard
phone_numbers = phone_regex.findall("+2437166293027 08155807084 08038672593"))
emails = email_regex.findall('gbae67@gmail.com tomi134@protonmail.com rosettadiamond@yahoo.com +2437068293037 xerox@filly.co.uk noahmonk@gmail.com')

# join each group together before adding it to the results variable
def join_group(list_container):
    """This function joins the parts of a group tuple together"""

    output = "" # output string
    
    for group_tuple in list_container:
        current_string = ""
        for element in group_tuple:
            current_string += element
        output += f"{current_string} "
    
    return output.strip()

print(join_group(emails))