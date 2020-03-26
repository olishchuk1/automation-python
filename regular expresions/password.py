import re
# creating some rules for password
password_regex = (
    re.compile(r'\d'), # a digit
    re.compile(r'[a-z]'), # a lowercase letter
    re.compile(r'[A-Z]'), # an uppercase letter
    re.compile(r'.{6,}'), # length six and more
    re.compile(r'!|@|#|$|%|^|&|\*|(|)|_|\+|=|-'), # a special symbol
    re.compile(r'.{12,}')  # length 12 and more
    )

password  = input()

counter = 0
for rx in password_regex:
    # counts how many rules are performed
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
