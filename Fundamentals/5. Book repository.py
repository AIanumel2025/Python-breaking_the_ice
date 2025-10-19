# Book repository: A simple book programme which allows you to store books
# Utilized code to populate a dictionary called 'books'
# User inputs a book, input is stored as a string in variable 'entry'. Programme could be refined to accept Sentence case inputs
# Programme checks to see if book already exists in the dictionary
# Program can be looped to allow a certain number of entries at any point in time


books = {1: 'Things fall apart', 2: 'Ancestral sacrifice', 3: 'What to think about machines that think', 4: 'Personal property'}

print('Welcome! Populate me!')
entry = input()

if books.key(entry):
    print(entry)
else:
    print('No sorry, try again')
    
    
# Feedback, comments all welcome!
