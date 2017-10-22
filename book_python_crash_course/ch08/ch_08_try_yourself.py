# (1) Message - Create a function to display a simple message

# def display_message():
# 	'''Display message that suggests what we are learning in this chapter'''
# 	print('\nWe are learning about functions in this chapter')

# display_message()

# (2) Favorite Book - Create function to display favorite book by accepting
#     parameters passed as an argument in the function call

# def favorite_book(title):
#     '''Display message regarding favorite book'''
#     message = 'One of my favorite books is ' + title.title()
#     print('\n' + message)

# favorite_book('the outsiders')

# (3) T-Shirt
# def make_shirt(size, message):
#     '''Display message of shirt size and message'''
#     message = ('Congrats, you have ordered the ' + size.title() + ' t-shirt '
#     + ' with the message of "' + message + '".')
#     print('\n' + message)


# make_shirt('m', 'Luke, I am your father')
# make_shirt(message = 'Never take sides against the family', size = 'XL')

# (4) Large Shirts
# def make_shirt(message, size = 'L'):
#     '''Display message of shirt size and message'''
#     message = ('Congrats, you have ordered the ' + size.title() + ' t-shirt '
#     + ' with the message of "' + message + '".')
#     print('\n' + message)


# make_shirt('I love python')
# make_shirt('With your powers combined, I am captian planet!', 'M')


# (5)  Cities

def describe_city(city, country = 'Brazil'):
    '''Create funtion to describe your city'''
    message = city + ' is in ' + country
    print(message)

describe_city('Sao Paolo')
describe_city('Rio')
describe_city('Manilla', 'Phillipines')
