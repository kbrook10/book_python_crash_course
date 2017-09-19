# (1) Try it yourself

# (4-3) Counting to Twenty

# numbers_1_to_20 = [number for number in range(1,21)]
# print(numbers_1_to_20)

# (4-4) One Million

# numbers_1_to_one_million = [number for number in range(1,1000001)]
# print(numbers_1_to_one_million)
# print(min(numbers_1_to_one_million))
# print(max(numbers_1_to_one_million))
# print(sum(numbers_1_to_one_million))

# (4-6) Generate list of odd numbers

odd_numbers = [number for number in range(1,20,2)]
print(odd_numbers)

# (4-7) Generate list of multiples of 3, from 3 to 30

multiples_of_3 = [number for number in range(3,30,3)]
print(multiples_of_3)

# (4-8) Generate list of cubes 
cubes = [number**3 for number in range(1,11)]
print(cubes)