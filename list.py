#Basic List Operation 

fruits = ['orange', 'banana', 'apple', 'cherry', 'plum', 'mango', 'berry']
fruits.append('pineapple')

print(fruits[3 :])
print(fruits[2 : 6])

#list Manipulation 

first = [1, 3, 5, 7, 9, 11]
second = [2, 4, 6, 8, 10, 12]

third = first.__add__(second)
print(sorted(third))
print(first * 3)

# Nested List 
nums = [
    [1, 3, 5, 7, 10],
    [2, 4, 6, 8, 10],
    [5, 10, 15, 20, 25]
]
print(nums)