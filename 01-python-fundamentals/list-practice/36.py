#36. Create a list and remove all odd numbers.
numbers = [10, 15, 20, 25, 30, 35, 40]
result = []
for number in numbers:
    if number % 2 == 0:
        result.append(number)
print(result)