# (1) Modifying the content of lists.

## Start with some designs that need to be printed...
unprinted_designs = ['iphone case', 'robot penant', 'dodecahedron']
completed_models = []

## Simulate printing each design, until none are left
while unprinted_designs:
	current_design = unprinted_designs.pop()

	## Simulate generating the 3D print
	print('\nPrinting model: ' + current_design)
	completed_models.append(current_design)

## Display all generated modesl

print('\nThe following models have been generated:')
for completed_model in completed_models:
	print('\t' + completed_model)
