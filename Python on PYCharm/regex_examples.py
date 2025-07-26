import re

 # Matches a U.S. phone number in the format 123-456-7890
phone = "123-456-7890"
#phone = "0092455368"
pattern = re.findall(r'\d{3}-\d{3}-\d{4}',phone)
print(pattern)

gmail = "abc@gmail.com"
#gmail = "Yemi@yemi@gmail.com"
# gmail = "tolu@gmail.com"
patternII = re.findall(r'(^[\w@][a-z]+@gmail| yahoomail\.[a-z]+)', gmail)
print(patternII)

# Count and return words that starts with uppercase
text = "Alice and Bob are Good Friends."
pattern_III = re.findall(r'\b[A-Z][a-z]+\b', text)
print(pattern_III)

# Split sentence into words ignoring punctuations
sentence = "Hello! How are you doing?"
patternIV = re.findall(r'[A-Za-z]\w+', sentence)
print(patternIV)