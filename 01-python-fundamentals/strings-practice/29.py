# Q29. Replace a word with another word in a sentence.

sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
result=sentence.replace(old_word,new_word)
print("Modified sentence :",result)