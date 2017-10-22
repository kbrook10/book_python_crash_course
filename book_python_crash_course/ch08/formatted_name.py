# (1) Using the return statement to send value from inside function, back to
#     the line that called the function...

# def get_formatted_name(first_name, last_name):
#     '''Return a full name neatly formatted'''
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# f_name = input('What is your favorite musicians first name? ')
# l_name = input('What is your favoriate musicians last name? ')

# musician = get_formatted_name(f_name, l_name)

# print(musician)

# (2) Incorporating Optional Arguments

def get_formatted_name(first_name, last_name, middle_name = ''):
    '''Return a full name neatly formatted'''

    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

f_name = input('What is your favorite musicians first name? ')
m_name = input('What is your favorit musicians middle name? ')
l_name = input('What is your favoriate musicians last name? ')

musician = get_formatted_name(f_name, l_name, m_name)

print(musician)