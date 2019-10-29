# This is a guess the number game.
import random
print('Hello! What is your name?')
myName = input()
number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
guess = 0
guessesTaken = 0
while guessesTaken < 6:
    guessesTaken = guessesTaken +1
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    if guess < number:
        print('You guess is too low')
    if guess > number:
        print('You guess is too high')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)



