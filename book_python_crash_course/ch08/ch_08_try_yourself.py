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

# def describe_city(city, country = 'Brazil'):
#     '''Create funtion to describe your city'''
#     message = city + ' is in ' + country
#     print(message)

# describe_city('Sao Paolo')
# describe_city('Rio')
# describe_city('Manilla', 'Phillipines')


# (6) City Names
# def city_country(city, country):
#     message = '"' + city.title() + ', ' + country.title() + '"'
#     return message

# print(city_country('nashville', 'United States'))
# print(city_country('Sao Paolo', 'Brazil'))
# print(city_country('Hong Kong', 'China'))


# (7) Album
# def make_album(artist_name, album_title, tracks = ''):
#     '''Build a dictionary that describes an album'''
#     album = {'artist name': artist_name, 'album title': album_title}
#     if tracks:
#         album['tracks'] = tracks
#     return album

# print(make_album('miles davis', 'blue like jazz'))
# print(make_album('outkast', 'speaker boxx'))
# print(make_album('michael jackson', 'thiller'))    
# print(make_album('lil wayne', 'tha block is hot', 12))

# (8) User Album

# def make_album(artist_name, album_title, tracks = ''):
#     '''Build a dictionary that describes an album'''
#     album = {'artist name': artist_name, 'album title': album_title}
#     if tracks:
#         album['tracks'] = tracks
#     return album

# while True:
#     print('\nPlease enter your favority album name and author title')
#     print('(enter \'q\' at any time to quit)')

#     art_name = input('Artist name: ')
#     if art_name == 'q':
#         break
#     alb_name = input('Album name: ')
#     if alb_name == 'q':
#         break

# artist_album_name = make_album(art_name, alb_name)


# print(make_album('miles davis', 'blue like jazz'))
# print(make_album('outkast', 'speaker boxx'))
# print(make_album('michael jackson', 'thiller'))    
# print(make_album('lil wayne', 'tha block is hot', 12))
# print(artist_album_name)

# (8-9) Magicians
# magicians = ['jack the great', 'john the fond', 'jill the will']

# def show_magicians(magicians):
#     '''Print the names of all the magicians'''
#     for magician in magicians:
#         print('It is our pleasure to introduce to you... ' + magician.title())

# show_magicians(magicians)
# print('That is all folks!')

# (8-10) Great Magicians
# magicians = ['jack the great', 'john the fond', 'jill the will']

# def make_great(magicians):
#     '''Add Great to the names of the magicians'''
#     great_magicians = []

#     while magicians:
#         current_magician = magicians.pop()
#         current_magician += ' The Great'
#         great_magicians.append(current_magician)

#     show_magicians(great_magicians)

# def show_magicians(magicians):
#     '''Print the names of all the magicians'''
#     for magician in magicians:
#         print('It is our pleasure to introduce to you... ' + magician.title())

# make_great(magicians)
# print('That is all folks!')


# (8-11) Unchanged Magicians
magicians = ['jack the great', 'john the fond', 'jill the will']

def make_great(magicians):
    '''Add Great to the names of the magicians'''
    great_magicians = []

    while magicians:
        current_magician = magicians.pop()
        current_magician += ' The Great'
        great_magicians.append(current_magician)

    show_magicians(great_magicians)

def show_magicians(magicians):
    '''Print the names of all the magicians'''
    for magician in magicians:
        print('It is our pleasure to introduce to you... ' + magician.title())


list_copy = magicians[:]
make_great(list_copy)
show_magicians(magicians)
show_magicians(list_copy)
print('That is all folks!')