"""
Text Analyzer

Difficulty: 1/10

Comments: This program analyzes a given text and provides statistics about its characters, words, and letter cases.
It counts the total number of characters and words, as well as the number of uppercase, lowercase, and special
characters in the text.
"""
uppercase_count, lowercase_count, special_count = 0, 0, 0

text = input("Insert text >")
characters = len(text)
words = len(text.split())
print(f"The amount of the characters in this text are {characters}")
print(f"The amount of the words in this text are {words}")

for letter in text:
    if letter.isupper():
        uppercase_count += 1
    elif letter.islower():
        lowercase_count += 1
    else:
        special_count += 1

print(f"The amount of the uppercase letters in this text are {uppercase_count}")
print(f"The amount of the lowercase letters in this text are {lowercase_count}")
print(f"The amount of the special letters in this text are {special_count}")
