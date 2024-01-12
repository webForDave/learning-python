#creating an empty set
names = set()

#adding elements to an empty set with the add method
names.add('David')

#adding multiple elements to a set using the update method
names.update(['Kenise', 'John', "Bill"])
print(names)

friends = {'Kenise', 'Rob', 'Victor'} 

#finding the union of two sets
everyone = names.union(friends)
print(everyone)

#finding the intersection between two sets
mutual = names.intersection(friends)
print(mutual)

#finding the difference between two sets
odd_person = names.difference(friends)
print(odd_person)


#defining a range of numbers
sequence = range(10, 25)
print(sequence)

# userInput = int(input('Enter a randon number : '))

# if userInput <= 0 :
#     print('Invalid number, start from 1')

# elif userInput in sequence :
#     print('You guessed right, you\'re in range')

# elif userInput not in sequence :
#     print('Wrong, too high')




#-------------EXERCISE---------------
    
a = {'apple', 'mango', 'pear', 'carrot'}
b = {2, 4, 6, 8 }
c = {'MTH', 'CSC', 'BIO', 'STAT'}

_a_and_b = a.union(b)
print(_a_and_b)

print(c.difference(_a_and_b))

a.remove('mango')
print(a)

b.add(10)
print(b)