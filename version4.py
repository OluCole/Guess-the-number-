import random as rd

counter = 1
guesses = []
mumber = rd.randint(1,10)

print("Lets play guess the number! I will have a number in mind from one  to ten.")
print("When you think you know the number I have in mind, type it!")

print(mumber)

while len(guesses) < 5:
   print(f"You have already guessed: {guesses}")
   number = int(input("Type the number you guessed!: "))
   guesses.append(number)

   if mumber == number:
      print("You win!")
      break

   counter += 1
