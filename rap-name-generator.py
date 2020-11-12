# Guided Exploration No. 3
# David Alyabyev

# import the random library
import random

# create emtpy list to store all rap names in
possible_names = []

# open new file where we can store the rap names created by this program
outputFile = open('rap-names-output.txt', 'w')

# open file for read access
with open('rap-names.txt', 'r') as dataFile:
    # loop through each line in the file that we opened to read one line at a time
    for name in dataFile:
        # append the possible names to the possible names list without a newline
        possible_names.append(name.rstrip())

# user input for how many names should be created
count = int(input('How many rap names would you like to create? '))
# user input for how many parts the name should contain
parts = int(input('How many parts should the name contain? '))

# generate total number of names that the user defined earlier
for i in range(count):
    # new list to hold the part of the rap name
    name_parts = []
    # iterate for the number of parts per name as defined by the user
    for j in range(parts):
        # generate random number to get that name from the possible names list and append to the name parts list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

    # write the completed rap name to the file after joining the name parts with spaces in between and a new line after the name has completed
    outputFile.write(f"{' '.join(name_parts)}\n")
    # print the completed rap name after joining the name parts with spaces in between and a new line after the name has completed
    print(f"{' '.join(name_parts)}")

# close the file with all the completed rap names
outputFile.close()
