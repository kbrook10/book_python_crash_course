# (1) Modifying the content of lists.

# Add Import statement to have Python to copy functions from printing_function
# module to this file...

# import printing_functions
# from printing_functions import printing_models
# from printing_functions import printing_models as pm
# import printing_functions as pf
from printing_functions import *

## Start with some designs that need to be printed...
unprinted_designs = ['iphone case', 'robot penant', 'dodecahedron']
completed_models = []

## Call function

printing_models(unprinted_designs, completed_models)


