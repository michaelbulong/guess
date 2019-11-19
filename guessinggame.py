import random

guessesTaken = 0

number = random.randint(1, 25)
print( "alright bro, im thinking of a number 1 to 25")

while guessesTaken < 10
    print ("take a guess")
    guess = input()
    guess = int(guess)