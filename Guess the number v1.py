import random

print("Lets play guess the number! I will have a number in mind from one  to ten.")
print("When you think you know the number I have in mind, type it!")


mumber = random.randint(1,10)
print(mumber)

i = int(input("Type the number you guessed!: "))

if i == mumber:
  print("You guessed it!")
else:
  print("Try again!")
