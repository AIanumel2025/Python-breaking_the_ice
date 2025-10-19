# Name predictor: Applied regex; imported the re module
# Used regex to match last name against a regex expression

# User inputs their full name, program attempts to match last name (string) to a created regex
# If the last letter of the last name meets the 

import re

print('Hello, what is your name?:')
name1 = input()

print('Nice one ' + name1 + ' I can predict your last name! What is its first letter?:')
lastletter = input()

# predict my last name

nameregex = re.compile(r'^A\w+')
lastnamem = nameregex.search('Anumel')

if lastletter == 'A' and lastnamem: 
    print('Your last name is ' + lastnamem.group() + '!')
else:
    print('Aww dang, I missed it! I can predict your age in 3 years. How old are you?:')
    age = input()
    print('Cool! you are going to be ' + str(int(age) + 3) + ' in 3 years!')

    print('Thanks for talking to me! Have a great day ' + name1 +  lastnamem.group() + '!')
    
