#19. Create a list of 10 numbers and remove duplicates
numbers=[1,2,3,2,2,3,4,5,6,7]
unique=[]
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)