def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide (100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, typ it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
# what = add(35, subtract(74, multiply(180,25)))
# what = add(35, subtract(74,4500))
# what = add(35, -4426)
# what = -4391

print("That becomes: ", what, "Can you do it by hand?")
