# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits

fruits= ['apple', 'banana', 'grapes', 'kiwi', 'avocado', 'pineapple']

# TODO: Add a fruit to the end of the list

fruits.append('orange')


# TODO: Insert a fruit at the beginning of the list
# fruits.insert(0,'pear') , Alternatively use this way

fruits = ['pear'] + fruits


# TODO: Remove a fruit from the list

fruits.remove("kiwi")

# TODO: Print the modified list

print(fruits)
#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5

numbers= [1,2,3,4,5]

# TODO: Create a new list with each number squared

squares= [1**2, 2**2, 3**2, 4**2, 5**2]

# TODO: Find the sum and average of the original numbers


total = sum(numbers) 
average = sum(numbers)/len(numbers)

# TODO: Print the results

print(f"the sum of the original numbers is {total} and average is {average}")

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals

my_dictionary= {'England':'London',
                'Germany':'Berlin',
                'France':'Paris',
                'Italy':'Rome',
                'South Africa':'Pretoria'}



# TODO: Add a new country-capital pair

my_dictionary.update({'Japan':'Tokyo'})

# TODO: Update the capital of an existing country

my_dictionary.update({'South Africa':'Cape Town'})

# TODO: Remove a country-capital pair

my_dictionary.pop('Japan')

# TODO: Print the modified dictionary

print(my_dictionary)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors

fruit_colours= {'Apple':'Red',
                'Banana':'Yellow',
                'Grapes':'Green',
                'Strawberry': 'Red',
                'Blueberry' :'Blue'}

# TODO: Print all the fruits (keys)

for key in fruit_colours:
     print(key)

#print(fruit_colours.keys())

# TODO: Print all the colors (values)

for values in fruit_colours.values():
    print(values)

#print(fruit_colours.values())

# TODO: Print each fruit and its color

for key, value in fruit_colours.items():
    print(f"{key}: {value}")

# TODO: Check if a fruit is in the dictionary and print its color

check = 'Strawberry'

if check in fruit_colours:
    print(f"The color of {check} is {fruit_colours[check]}.")
else:
    print(f"{check} is not in the dictionary.")