
# ==================
# 2_variables.py
# ==================

# Variables (Strings, Integers), Concantenation, Precedence, Interger operations and expressions
# Print options (range, Specify start & end points), String operators, Multiplying strings, using "in"


# Sting variables
greeting = "Hello"
name = "Bruce"

#String variables can be concatinated
print(greeting + ' ' + name)
print()

# Integer variable is a whole number and run faster
age = 24
age2 = 50
print(age)
print()

# Integer variables can be added together.
print(age + age2)

# Integer operations and expressions
# Expression is something that can be calculated to return a value.

a = 12
b = 3
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Divisiion. Result will be float (with decimal)
print(a // b) # Division but result will be interger (no decimal)
print(a % b) # Modulus. What remains after division
print()

# Uses of division with // where it returns integer
# This can be used in for loops which require integers

for i in range(1, a//b): # If you use a/4 (4.0), you will get error
    print(i)

print()

# Precedence
a = 12
b = 3
print(a + b / 3 - 4 * 12) # Multiplication and divisions done first
print()
print((((a + b) / 3) - 4) * 12) # using brackets to overide operator predence
print()

# Another example to overide operator precedence

c = a + b
d = c / 3
e = d - 4
print(e * 12)
print()

# Print options for String operator
parrot = "Norwegian Blue"
print(parrot) # Prints the whole string
# Specifying character positions to print.
print(parrot[0]) # Prints first charactor in string. Starts with 0
print(parrot[1]) # Prints second charactor in string
print(parrot[2]) # Prints third charactor in string
print()
print(parrot[-0]) # Cannot use -0 to start from end.
print()

# Printing from end of line
print(parrot[-1]) # Prints from end. Start with e as 1
print(parrot[-2]) # Prints second charactor from end
print(parrot[-3]) # Prints third charactor from end
print(parrot[-4]) # Prints forth charactor from end
print()

# Printing a range
print(parrot[0:6]) # Prints a slice or range from 0 to 6th character
print(parrot[:6]) # If you don't specify start point, it starts from beginning
print()
print(parrot[6:]) # Starts from one after 6 to end if you don't specify endpoint
print()

# Printing a range starting from end of line
print(parrot)
print(parrot[-4:-1]) # Starts at 4 from end and ends at 1 from end
print(parrot[-4:-2]) # Starts at 4 from end and ends at 2 from end
print(parrot[-4:-3]) # Starts at 4 from end and ends at 3 from end
print()

# Specify start point, end point and increment
print(parrot)
print("6th Character starting at 0 is:" + ' ' +parrot[6])
print(parrot[0:6:2]) # Starts at 0, ends at 6 (not including 6), increment of 2
print(parrot[0:6:3]) # Starts at 0, ends at 6, increment 3
print()

# Uses of this range with 3 paramenters is to extract numbers
number = "9,123,456,789,123,456,789"
print(number)
print("we will extract commas from this number")
print(number[1::4]) # Starts at position 1, no endpoint, and increment by 4
print(number[1:20:4]) # Starts at 1, endpoint before 20, increment 4
print()
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers)
print(numbers[0::3]) # To extract only numbers and leave comma and spaces
print()

# String operator and string literal
string1 = "Good Morning " # String operator
string2 = "Maren"         # String operator
print(string1 + string2) # Need + sign when using string operator
print()
print("Good Morning " "Maren") # No need for + when using string literal
print()

# Multiplying strings
print("Hello " * 3) # Multiplying string Hello 5 times
print("Hello " *(3 + 2)) # Multiplying hello 5 times
print("Hello " *(3 * 2)) # Multiplying hello 6 times
print()

# Operator to check if one string is substring of another.
name = "Mwongera"
print(name)
print("Mwong" in name) # Checking if Mwong is in Mwongera (True)
print("era" in name) # Checking if era is in Mwongera (True)
print("Maren" in name) # Checking if Maren is in Mwongera (False)

