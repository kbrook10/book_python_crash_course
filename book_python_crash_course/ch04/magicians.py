# (1) Using 'for' loops to avoid repetition in code and prevent unnecessary code changes.
# the below for loop prints each magician in the list magicians

magicians = []

magicians.append('alice')
magicians.append('david')
magicians.append('carolina')

for magician in magicians:
	# print(magician)
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone, that was a great magic show!")


