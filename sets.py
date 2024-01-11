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