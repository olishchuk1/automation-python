import re
password_regex = (
    re.compile(r'\d'),
    re.compile(r'[a-z]'),
    re.compile(r'[A-Z]'),
    re.compile(r'.{6,}'),
    re.compile(r'!|@|#|$|%|^|&|\*|(|)|_|\+|=|-'),
    re.compile(r'.{12,}')
    )

password  = input()

counter = 0
for rx in password_regex:
    if rx.search(password):
        counter += 1

if counter <= 2:
    print('Your password is too weak')
elif 2 < counter <= 3:
    print('You passwors is weak')
elif 4 < counter <= 5:
    print('Your password is medium')
else:
    print('Your password is hard')
