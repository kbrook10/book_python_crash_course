# Create module that includes one function to print models

def printing_models(designs ,completed_models):
	## Simulate printing each design, until none are left
	while designs:
		current_design = designs.pop()

		## Simulate generating the 3D print
		print('\nPrinting model: ' + current_design)
		completed_models.append(current_design)

	## Display all generated modesl

	print('\nThe following models have been generated:')
	for completed_model in completed_models:
		print('\t' + completed_model)