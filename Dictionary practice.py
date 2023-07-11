# Write your code here :-)DICTIONARIES store connections between pieces of information. Each item in a dictionary is a key-value pair.
#Dictionary paris are saved between curly brackets.

# A simpe dictionary
alien = {'color': 'green', 'points':5}

#this is a blank line
print()

#accessing a value: use the Variable name and within square brackets choose the first part of the value pair.
print("The alien's color is " + alien['color'])

#adding a new key-value pair

alien['x_position'] = 0

print(alien)

#new value pai is added.
#this is a blank line
print()

#LOOPING THROUGH ALL KEY(color)-VALUE(Green) PAIRS
fav_numbers = {'eric': 17, 'ever':4}
for name, number in fav_numbers.items():
    print(name+ ' loves '+ str(number))

#this is a blank line
print()

#Looping through all the values


fav_numbers = {'eric': 17, 'ever':4}
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')

#this is a blank line
print()

members_age = {'john': 45, 'Joseph': 55}
for number in members_age.values():
    print(str(number) + ' is a favorite')
