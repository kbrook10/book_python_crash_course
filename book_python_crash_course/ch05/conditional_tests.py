# (5-2) More Conditional Tests -

print(len('This is a great day') == len('Tthis is not a bad day'))

string_1 = 'Jack and Jill went up the Hill'
string_2 = 'jack and jill went up the hill'

print( string_1.lower() != string_2)

number_0 = 10
number_1 = 15
number_2 = 20
number_3 = 25
number_4 = 30

print(number_0 != number_1)

print((number_1 + number_0) == number_3)

print((number_1 <= number_2) and (number_0 <= number_4))

print((number_4 >= number_2*3) or (number_3 >= number_0**2))

cars = ['bmw', 'audi', 'nissan', 'ford', 'gmc']

print('Is Nissan in the list of cars')
print('nissan' in cars)

print('Is GMC not in the list of cars')
print('gmc' not in cars)