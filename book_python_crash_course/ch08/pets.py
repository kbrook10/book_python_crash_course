# (1) Using Positional Arguments with Functional Parameters

# def describe_pet(animal_type, pet_name):
#     '''Display type of animal and pet name'''
#     print('\nI have a ' + animal_type.title() + '.')
#     print('My ' + animal_type.lower() + '\'s name is ' + pet_name.title() + '.')

# describe_pet(animal_type = 'bird', pet_name = 'Oliver')
# describe_pet('dog', 'Willie')

# (2) Working with default arguments

def describe_pet(animal_type , pet_name):
    '''Display type of animal and pet name'''
    print('\nI have a ' + animal_type.title() + '.')
    print('My ' + animal_type.lower() + '\'s name is ' + pet_name.title() + '.')

describe_pet()