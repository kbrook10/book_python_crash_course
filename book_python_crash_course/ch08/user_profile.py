# (1) Build function to accept various arguments

def build_profile(first, last, **user_info):
	'''Build a dictionary to store everything about the user'''

	# Create the structure for the user profile
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last

	# Create the structure to accept information that is unknown
	for key, value in user_info.items():
		profile[key] = value

	# Return the completed profile to the calling function
	return profile

# Call the build profile for new user
user_profile = build_profile('albert', 'eistein', location = 'princeton',
				field = 'physics')

# Print the end result
print(user_profile)