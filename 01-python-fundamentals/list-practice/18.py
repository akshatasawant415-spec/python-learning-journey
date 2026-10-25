#18. Take user input to create a list and display it.
numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)
print("List:", numbers)