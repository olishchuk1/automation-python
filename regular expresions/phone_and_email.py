import re, pyperclip

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# Create email regex
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2, 4})
    )''', re.VERBOSE)
# Find matches in clipboard text
text = str(pyperclip.paste())
text = 'help@nostarch.co help@nostarch.co help@nostarch.co (243)-253-1313 131 234-2344-2343, 432242, sfdsfsa@ds.cs asadw'
# Copy result to the clipboard
matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])
    
print(matches)
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
