import re

websideText = open("st georges.txt")
text = websideText.read()

phone_number = re.compile(r"\d\d\d \d\d\d\d \d\d\d\d")
print(phone_number.findall(text))
