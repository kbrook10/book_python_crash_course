# (1) Message - Create a function to display a simple message

def display_message():
	'''Display message that suggests what we are learning in this chapter'''
	print('\nWe are learning about functions in this chapter')

display_message()

# (2) Favorite Book - Create function to display favorite book by accepting
#     parameters passed as an argument in the function call

def favorite_book(title):
    '''Display message regarding favorite book'''
    message = 'One of my favorite books is ' + title.title()
    print('\n' + message)

favorite_book('the outsiders')