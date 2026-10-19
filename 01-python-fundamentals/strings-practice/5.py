# Q5. Count the number of consonants in a string.

text = input("Enter a string: ")

count = 0
for ch in text.lower():
    if ch not in "aeiou":
        count+=1
print("Number of consonents :",count)