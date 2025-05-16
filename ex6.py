types_of_people = 10
# Note: the f is required for variable interpolation
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
# Note: single quotes are just for printing
# No difference between single and double quotes in python
print(f"I also said: '{y}'")

hilarious = False
# The {} is a placeholder for a print statement later where you can provide a variable
joke_evaluation = "Isn't that joke so funny?! {}"

# Now let's print the joke_evaluation with the variable hilarious
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
