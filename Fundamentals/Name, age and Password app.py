
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


