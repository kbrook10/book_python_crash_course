# Start w/ a list of unconfirmed users and an empty list of confirmed users.

unconfirmed_users = ['Jack', 'Joe', 'Diane', 'Spot']
confirmed_users = []

# Verify users within the unconfirmed users list and move to confirmed

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print('Verifying user: ' + current_user)
	confirmed_users.append(current_user)


# Display the list of confirmed users

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

