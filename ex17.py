from sys import argv
from os.path import exists

script, from_file, to_file = argv

# One-liner that is memory safe
with open(from_file) as in_file, open (to_file, 'w') as out_file:
    out_file.write(in_file.read())

# One-liner that is not memory safe and leaves the file open
#open(to_file, 'w').write(open(from_file).read())

# Code from the original exercise

#in_file = open(from_file)
#indata = in_file.read()

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to contine, CTRL-C to abort.")
#input()

#out_file = open(to_file, 'w')
#out_file.write(indata)


#print("Alright, all done.")

out_file.close()
in_file.close()

