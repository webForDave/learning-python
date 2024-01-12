# def add (num1, num2) :

#     print(num1 + num2)

# add(6, 4)

# def subtract (num1, num2) :

#     print(num1 - num2)

# subtract(6, 4)

# def division (num1, num2) :

#     print(num1 // num2)

# division(6, 2)

# def multiplication (num1, num2) :

#     if num2 == 0 :
#         print('Err, you can\'t pass in 0')

#     else : 
#         print(num1 * num2)

# multiplication(6, 0)


def show_info (tv_show) :
    print(f'{tv_show["title"]} ({tv_show["initial_release"]}) - {tv_show["seasons"]} seasons')

show_info(tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
})


def palindromeChecker (word) :
    
    if word[ : : -1] == word :
        print(f'{word} is palindrome')
    else :
        print(f'{word} is not a palindrome')

palindromeChecker(input('Enter a word : \n'))