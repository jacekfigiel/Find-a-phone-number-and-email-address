import re

websideText = open("st georges.txt")
text = websideText.read()

phone_number = re.findall(r"\d\d\d \d\d\d\d \d\d\d\d", text)
for n in phone_number:
    print(n)

email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
for e in email:
    print(e)
