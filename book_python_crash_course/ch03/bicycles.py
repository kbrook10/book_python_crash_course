bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])

# Format the element using the title method
print(bicycles[0].title())

# Obtain the 1 and 3 elements in the list
print(bicycles[0].title())
print(bicycles[2].title())

# Request the last item in the list
print(bicycles[-1].title())

# Try This Practice
#< --------------------- >

# 3-1 Names
names = ['Jack', 'Joe','Ted', 'Joseph']
print(names[0].title())
print(names[1].title())
print(names[-2].title())
print(names[-1].title())

# 3-2 Greetings
message = "The members of one of America's greatest families are " + names[0].title() + " Kennedy, who were loved by many and feared by others."
message1 = "The members of one of America's greatest families are " + names[1].title() + " Kennedy, who were loved by many and feared by others."
message2 = "The members of one of America's greatest families are " + names[-2].title() + " Kennedy, who were loved by many and feared by others."
message3 = "The members of one of America's greatest families are " + names[-3].title() + " Kennedy, who were loved by many and feared by others."

print(message)
print(message1)
print(message2)
print(message3)


# 3-3 Your Own List
cars = ['Telsa', 'Honda', 'Nissa', 'Mazda', 'Ford', 'Toyota']
message = 'I will own a ' + cars[0].title() + ' SUV in two years, (i.e. 2019)'
print(message)




