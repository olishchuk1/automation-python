import re, pyperclip

# Create website regex.
website_regex = re.compile(r'''(
    http(s)?://
    (w{3}.)?
    [a-zA-Z0-9]
    [a-zA-Z0-9-%+-]+ 
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)


# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []

for groups in website_regex.findall(text):
    matches.append(groups[0])

# Copy result to clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No websites found.')
