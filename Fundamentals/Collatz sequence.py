# A typical Collatz sequence code: Code allows input of a positive number. 
# If the number is even it is divided by 2.
# If odd, it is multiplied by 3 with one added to it

# Defined a function collatz(number) and utilized if conditionals to apply the rule
# Looped the program until final number outputted was 1

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    print('Enter your number here')
    collatz(int(input()))
    

# Feedback? Thoughts, suggestions all welcome!
