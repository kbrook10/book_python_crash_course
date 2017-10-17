# (1) Using Positional Arguments with Functional Parameters

def describe_pet(animal_type, pet_name):
    '''Display type of animal and pet name'''
    print('\nI have a ' + animal_type.title() + '.')
    print('My ' + animal_type.lower() + '\'s name is ' + pet_name.title() + '.')

describe_pet('bird', 'Oliver')
