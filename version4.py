import random as rd
counter = 1
mumber = random.randint(1,10)
guesses = []

print("Lets play guess the number! I will have a number in mind from one  to ten.")
print("When you think you know the number I have in mind, type it!")
print(mumber)
while len(guesses) < 5:
   mumber = int(input("Type the number you guessed!: "))
   guesses.append(mumber)
   print(guesses)
