# Q38. Find the shortest word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()
if words:
    shortest=words[0]
    for ch in words:
        if len(ch)<len(shortest):
            shortest=ch
    print("Shortest word :",shortest)
else:
    print("No words found")