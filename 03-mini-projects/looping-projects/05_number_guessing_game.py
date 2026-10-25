secret_number=37
attempts=0
won=False
while attempts<5 and won==False:
    guess=int(input("Enter your guess :"))
    attempts=attempts+1
    if guess==secret_number:
        print("Correct!! you won")
        won=True
        break
    elif guess<secret_number:
        print("Too low!")
    else:
        print("Too High !!")
if won == False:
    print("Game over! The secret number was:", secret_number)
print("Attempts used:", attempts)