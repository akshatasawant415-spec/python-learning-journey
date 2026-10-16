import random as r
print("===== Password Generator =====")
while True:
  pass_len=int(input("Enter password length: "))
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
  password=""
  for ch in range(pass_len):
    rand_char=r.choice(characters)
    password+=rand_char
  print("Your password is :",password)