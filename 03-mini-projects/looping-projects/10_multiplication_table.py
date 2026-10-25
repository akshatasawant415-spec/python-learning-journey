number = int(input("Enter a positive integer: "))
if number <= 0:
    print("Invalid number")
    exit()

print("Multiplication Table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

start = int(input("Enter range starting number: "))
end = int(input("Enter range ending number: "))
if start > end:
    print("Invalid range")
    exit()

even_count = 0
odd_count = 0
total_sum = 0
for i in range(start, end + 1):
    total_sum = total_sum + i

    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
print("Sum of range:", total_sum)
