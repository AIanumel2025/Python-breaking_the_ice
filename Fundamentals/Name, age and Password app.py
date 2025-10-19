# Simple authentication programme: Allows user to validate authentication by providing name, age and correct password

# User inputs their name first
# If the name is not Tony, the program denies the user access and loops for another try
# Program repeats for age and password, if both are incorrect, user is denied access
# Program ends when user guesses all entries provided correctly (name, age, password)

name = 'Tony'
age = 'Thirty six'
password = 'Bomb'
print('Hello! Please input your name..')
name = input()
while name != 'Tony':
      print('Access Denied, Try again.')
      name = input()
    
print('Thank you, what about your age?')
age = input()
while age != 'Thirty six':
    print('Error!')
    age = input()
  
print('Great, now your Password?')
password = input()
while password != 'Bomb':
    print('Nope!')
    password = input()
    
print('Thank you SIR!')

# Feedback, comments all welcome!
