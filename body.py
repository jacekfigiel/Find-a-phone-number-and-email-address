import re, pyperclip
"""just press CTRL+a then CTRL+c and run a program, list is ready"""

text = str(pyperclip.paste())

phone_number = re.findall(r"\d\d\d \d\d\d\d \d\d\d\d", text)
for n in phone_number:
    print(n)

email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
for e in email:
    print(e)
