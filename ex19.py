from sys import argv

num_to_test = int(argv[1])
print(f"Testing if {num_to_test} is in the Fibonacci sequence.")

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def next_number_in_sequence(num1,num2):
    return num1 + num2

def is_fibonacci_sequence_number(num_test):
    num1 = 0
    num2 = 1

    if(num_test == num1):
        return True
    else:
        while (num2 <= num_test):
            if(num_test == num2):
                return True
            else:
                previous_number_in_sequence = num2
                num2 = next_number_in_sequence(num1,num2)
                num1 = previous_number_in_sequence
                print(f"Fibonacci Sequence {num1} - testing {num_test}")

is_fibonacci_number = is_fibonacci_sequence_number(num_to_test)
if(is_fibonacci_number):
    print(f"{num_to_test} is in the fibonacci sequence.")
else:
    print(f"{num_to_test} is not in the fibonacci sequence.")
