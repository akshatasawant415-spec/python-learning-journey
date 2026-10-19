# Q37. Find the longest word in a sentence.

sentence = input("Enter a sentence: ")
words=sentence.split()
if words:
    longest=words[0]
    for word in words:
        if len(word)>len(longest):
            longest=word
    print("Longest word :",word)
else:
    print("No words found")