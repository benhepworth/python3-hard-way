from sys import argv

# get arguments from command line
script, filename = argv

# open the file
txt = open(filename)

print(f"Here's your file {filename}")
# read and print the file
print(txt.read())
txt.close()

# as user for input for another file
print("Type the filename again:")
file_again = input("> ")

# read the file
txt_again = open(file_again)

# print the file
print(txt_again.read())
txt_again.close()
