# Number guessing game: Learnt and applied module importation. 
# Utilized the random module, for loop, conditional statements, continue and break statements
# Utilized the range methods to loop number of user inputs 

# Player inputs any random number between 1 and 20 into console
# if statements to determine is secret number is too high or low
# If correct number is determined within specified range, programme ends successfully with the number of guesses printed to obtain
# Program ends successfully if correct number is not entered within specified range

import random
secretNumber = random.int(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.

for guessesTaken in range(1, 7):
  print('Take a guess.')
  guess = int(input())

  if guess < secretNumber:
    print('Your guess is too low.')
  elif guess > secretNumber:
    print('Your guess is too high.')
  else:
    break

if guess == secretNumber:
  print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
  print('Sorry. The number I was thinking about was ' + str(secretNumber))


# Feedback, comments all welcome!
