text=input("Enter your paragraph :")
characters=len(text)
print("Characters are :",characters)
words=text.split()
print("words are :",len(words))
full_stops = text.count(".")
exclamations =text.count("!")
questions = text.count("?")
sentences = full_stops + exclamations + questions
print("Sentences are:", sentences)
vowel=0
consonents=0
digit=0
special_char=0
for i in text :
    if i in "AEIOUaeiou":
        vowel=vowel+1
    elif i.isalpha():
        consonents=consonents+1
    if i.isdigit():
        digit=digit+1
    elif not i.isalnum() and not i.isspace():
        special_char=special_char+1
print("Vowels:", vowel)
print("Consonants:", consonents)
print("Digits:", digit)
print("Special characters:", special_char)
uppercase=text.upper()
lowercase=text.lower()
print("Uppercase :",uppercase)
print("Lowercase :",lowercase)
word=input("Enter word you want to search :")
if word in words:
    print("Word found ")
else:
    print("Not found ")
word=input("Enter word you want to count :")
words=text.split()
occurance=words.count(word)
print(f"{word} appeared {occurance} times ")
words=text.split()
cleanted_text=" ".join(words)
print(cleanted_text)