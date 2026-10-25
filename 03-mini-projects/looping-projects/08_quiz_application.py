score = 0
total_questions = 5

questions = [
    ("What is 2 + 2? ", "4"),
    ("What is the color of the sky? ", "blue"),
    ("What is the color of grass? ", "green"),
    ("What is the color of milk? ", "white"),
    ("What is the color of sunset? ", "orange")
]

for question, correct_answer in questions:
    answer = input(question).strip().lower()

    if answer == correct_answer:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect!")

percentage = (score / total_questions) * 100

print("Score:", score, "/", total_questions)
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good!")
else:
    print("Keep Practicing!")
