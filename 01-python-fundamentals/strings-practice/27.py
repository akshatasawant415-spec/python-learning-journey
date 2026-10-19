# Q27. Check whether a word exists in a sentence.

sentence = input("Enter a sentence: ")
word = input("Enter a word to search for: ")
if word in sentence:
    print("Word exists")
else:
    print("Word does not exist")