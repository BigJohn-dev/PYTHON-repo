import re

sentence = "The silent boy is sic today, call this number 1234567890"

# pattern = re.findall(r'\b[A-Za-z]+\b', sentence)
# pattern = re.compile('[A-Za-z]+')

pattern = re.compile(r'[^0-9]+')
match = pattern.findall(sentence)
print(match)