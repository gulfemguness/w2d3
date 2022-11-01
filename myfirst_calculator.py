# def printName(name):
#     print(f"Hello Mr/Ms {name}...we've been waiting for you!")

#                                                         Hi! :)

"""
1) Build a Shopping Cart
"""




"""
2) Create a Module in VS Code and Import It into jupyter notebook
"""

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area


# input =  Enter the length of the house
# 2nd input = Enter the width of the house
# output = the house is ... sq. ft.

# example output:  The square footage of a room 15 feet wide and 15 feet long is 225 square feet. 


def rectangle_area():
    length = float(input("Enter the length of the house: "))
    width = float(input("Enter the width of the house: " ))
    area = length * width
    print("The square footage of the house is", float(area) ,"sq. ft.")
    
rectangle_area()

    
    
# 2) Has a function to calculate the circumference of a circle
# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage
# 2 * pi * r

# input = Enter the radius of a circle:    
# output = The circumference of a circle is ....


def find_circumference():
    pi = 3.14
    r = float(input("Enter the radius of a circle: "))
    c = 2 * pi * r
    # return 2 * pi * r
    print("The circumference of a circle is", float(c) ,"cm.")
    
find_circumference()





# Note: (from doc_name import module_name)
