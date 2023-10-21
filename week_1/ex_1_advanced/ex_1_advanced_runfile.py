# EX_1 ADVANCED by Matias Medina Tanco
# "I pity the man who reads my code"

# Open the reference text files
file1 = open("references_1.txt", "r", encoding="utf8")
file2 = open("references_2.txt", "r", encoding="utf8")
# Read lines in the reference text files and save them in f1 and f2
f1 = file1.readlines()
f2 = file2.readlines()
# Close files so they're no longer in use by the program
file1.close()
file2.close()

# Create empty lists that will later be used to generate dictionaries
reference1_1 = []
reference1_2 = []
reference2_1 = []
reference2_2 = []

#######################################################################################################
### Process file 1

## Obtain numbers for reference 1
# Process the text in f1 and append it to the reference_1_1 list
for line in f1:
    # Use strip method to remove spaces at beginning and end of the strings
    reference1_1.append(line.strip())

# Define a separator
sep ="."

# Go through the elements of the list and remove all text after the dot separator so only the numbers are taken
for i in range(len(reference1_1)):
    reference1_1[i] = reference1_1[i].split(sep)[0]
    # Add a dot to each element in the list because .split() removes the separator
    # reference1_1[i] += "."

## Obtain citations for reference 1
# Process the text in f1 and append it to the reference_1_2 list
for line in f1:
    # Use strip method to remove spaces at beginning and end of the strings
    reference1_2.append(line.strip())

# Go through the elements of the list and remove all text after the dot separator so only the numbers are taken
for i in range(len(reference1_2)):
    reference1_2[i] = reference1_2[i].split(sep,1)[-1]

# Go through all the elements of the reference_1_2 list and remove all white spaces in the text
for i in range(len(reference1_2)):
    reference1_2[i] = reference1_2[i].replace(" ", "")

# Delete the first elements of these lists as they include the "References" text from the first line of the document
del reference1_1[0]
del reference1_2[0]

#######################################################################################################
### Process file 2 (Same process as before)

## Obtain numbers for reference 2
# Process the text in f1 and append it to the reference_1_1 list
for line in f2:
    # Use strip method to remove spaces at beginning and end of the strings
    reference2_1.append(line.strip())

# Define a separator
sep ="."

# Go through the elements of the list and remove all text after the dot separator so only the numbers are taken
for i in range(len(reference2_1)):
    reference2_1[i] = reference2_1[i].split(sep)[0]
    # Add a dot to each element in the list because .split() removes the separator
    # reference2_1[i] += "."

## Obtain citations for reference 1
# Process the text in f1 and append it to the reference_1_2 list
for line in f2:
    # Use strip method to remove spaces at beginning and end of the strings
    reference2_2.append(line.strip())

# Go through the elements of the list and remove all text after the dot separator so only the numbers are taken
for i in range(len(reference2_2)):
    reference2_2[i] = reference2_2[i].split(sep,1)[-1]

# Go through all the elements of the reference_1_2 list and remove all white spaces in the text
for i in range(len(reference2_2)):
    reference2_2[i] = reference2_2[i].replace(" ", "")
    # Remove at the beginning of the citations in this file as well
    reference2_2[i] = reference2_2[i].replace("\t", "")

# Delete the first elements of these lists as they include the "References" text from the first line of the document
del reference2_1[0]
del reference2_2[0]

#######################################################################################################

# Finally initialize the two reference dictionaries where the citation number is the key and the citation
# text is the value
refDictionary1 = dict(zip(reference1_1, reference1_2))
refDictionary2 = dict(zip(reference2_1, reference2_2))

# Create the "status" enumerated 1-60
status = {}
for i in range(1,61):
    status[i] = None

# Iterate through the two reference dictionaries using a for loop,
for k in refDictionary1:
    # if the strings of the references match exactly, set value to "GOOD"
    if refDictionary1[k] == refDictionary2[k]:
        status[int(k)] = "GOOD"
    else:
        # Use filter() function to create a filter object that only keeps characters that are not similar
        # in index in both strings
        difference = filter(lambda x: x[0] != x[1], zip(refDictionary1[k], refDictionary2[k]))
        # Use join() function to convert the filtered object to a string and assign value to status dictionary
        res = ''.join(x[0] for x in difference)
        status[int(k)] = str(res)


# Write the "ex_1_advanced_submit.txt" advanced submit file with the output from the status dictionary
with open("ex_1_advanced_submit.txt", "w", encoding="utf8") as f:
    for k in status:
        f.write(str(k))
        f.write("    ")
        f.write(str(status[k]))
        f.write("\n")
    f.close()
