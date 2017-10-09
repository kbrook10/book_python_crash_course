# (1) Be specific when using the input function to ensure user understands 
#     request

# name = input('Please enter your name: ')
# print('Hello, ' + name + '!')

# (2) Using variables with the input function

prompt = 'If you tell us who you are, we can personalize the messages you see'
prompt += '\nWhat is your first name? '

name = input(prompt)
print('\nHello, ' + name + '!')