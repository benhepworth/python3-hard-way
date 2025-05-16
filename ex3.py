print("I will now count my chickens:")

# Order of operations important
# Python follows PEMDAS
# Parentheses, Exponents, Multiplication and Division (left to right), Addition and Subtraction (left to right)
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

# division, modulus, then addition and subraction
# modulus fits into the "MD" in PEMDAS
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# no parenthesis, so order of operations
print("Is it true that 3 + 2 < 5 - 7?")

# print the result of the expression
print(3 + 2 < 5 - 7)

# print each side of the expression
print("What is 3 + 2?", 3+2)
print("What is 5 - 7?", 5-7)

print("Oh, that's why it's False.")

print("How about some more.")

# try some other comparison operators

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
