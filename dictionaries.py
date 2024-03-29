# song = {
#     "title": "The dark side of the Moon",
#     "artist": "Pink Floyd",
#     "year": '1973',

#     "songs": [
#         "Speak to Me",
#         "Breathe",
#         "On the Run",
#         "Time",
#         "The Great Gig in the Sky",
#         "Money",
#         "Us and Them",
#         "Any Colour You Like",
#         "Brain Damage",
#         "Eclipse"
#     ]

# }


# my_dict = {
#     "mango": 5,
#     "apple": 10,
#     "berry": 2
# }

# print(my_dict["berry"])

# my_dict["orange"] = 20
# my_dict["orange"] = 4
# del(my_dict["orange"])
# print(my_dict)

# for value in my_dict :
#     print(my_dict[value])



# if "mango" in my_dict :
#     print (True)

# else : 
#     print(False)

# print(len(my_dict))

# my_dict.clear()
# print(my_dict)


# person = {
#     "name": "David",
#     "age": 19,
#     "ninjas" : {
#         "yoshi": "black",
#         "ryu": "Red"
#     }
# }

# person["ninjas"]['dave'] = "Yellow"

# print(person["ninjas"])




#one way of creating a dictionary
man = dict([
    ("name", "David"),
    ("age", 19),
    ("country", "Nigeria")
])

#another way of creating a dictionary
details = dict(
    name = 'Sharon',
    age = 22,
    country = 'Nigria'
)

#accessing elements in a dictionary 
print(man["age"])
print(details["country"])


#adding an entry to a dictionary
man["married"] = False
details["married"] = True
print(man)
print(details)


#updating an entry
man["country"] = 'Austrailia'
details["country"] = 'Russia'


#deleting entries of a dictionary
del man["married"]
del details["married"]
print(man)
print(details)


#using integer as dictionary key
car = dict([
    (1, 1997),
    (2, 'Honda'),
    (3, 'Jackrel')
])
print(car)


#building a dictionary increamnetally
human = {}
human["name"] = 'Sara'
human["age"] = 50
human["spouse"] = 'Eric'
human["children"] = ['Sam', 'Jon', 'Ryu']
human["pets"] = dict(cat = 'Fido', dog = 'Sox')

#retreiving sub-list and sub-dictionary
print(human["children"][-1])
print(human["pets"]["dog"])

#built-in methods
print("spouse" in human)
print("gender" not in human)