#  (
#     "The Dark Side of the Moon",
#     "Pink Floyd",
#     1973,
#     (
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
#     )
#  )

song = {
    "title": "The dark side of the Moon",
    "artist": "Pink Floyd",
    "year": '1973',

    "songs": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]

}


my_dict = {
    "mango": 5,
    "apple": 10,
    "berry": 2
}

print(my_dict["berry"])

my_dict["orange"] = 20
my_dict["orange"] = 4
del(my_dict["orange"])
print(my_dict)

for value in my_dict :
    print(my_dict[value])


if 20 in my_dict:
    print('Yea')

else : 
    print('No')



if "mango" in my_dict :
    print (True)

else : 
    print(False)

print(len(my_dict))