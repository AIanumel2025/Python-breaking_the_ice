# Password Authenticator: Utilizes while loop and continue and break statements

# User inputs password into console
# If the name inputed is Joe, python reads the next line of code instead of looping back to primary prompt
# Same applies to subsequent lines of code. If password is inputted correctly, program ends successfully

while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':
    continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
      break
# Feedback, comments all welcome!
