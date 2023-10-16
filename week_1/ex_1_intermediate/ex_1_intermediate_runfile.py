# Initialize dictionaries to store references from the two files
# Key: Line number, Value: Reference text without whitespaces
ref1_dict = {}  # Creates an empty dictionary to hold references from the first file
ref2_dict = {}  # Creates an empty dictionary to hold references from the second file

# Initialize a dictionary to keep track of the comparison status
# Key: Line number, Value: List containing either 'GOOD' or differences
status = {}  # Creates an empty dictionary to store the results of the comparison
for i in range(1, 61):  # Goes through numbers 1-60 to populate status dictionary keys
    status[str(i)] = []  # Sets the value of each key to an empty list to store status info

# Open both files and read them line by line
with open("references_1.txt", "r") as f1, open("references_2.txt", "r") as f2:
    for i, (line1, line2) in enumerate(zip(f1, f2), 1):  # Reads both files line by line
        # Remove any trailing and internal whitespaces
        ref1_dict[str(i)] = line1.strip().replace(" ", "")  # Populates the first dictionary with cleaned-up text from the first file
        ref2_dict[str(i)] = line2.strip().replace(" ", "")  # Populates the second dictionary with cleaned-up text from the second file

# Loop through the dictionaries to compare each line
for key in ref1_dict:  # Goes through each key (which is the line number) in the first dictionary
    if ref1_dict[key] == ref2_dict[key]:  # Compares the values (text content) of both dictionaries for each line
        status[key].append("GOOD")  # Appends "GOOD" to the list value of the corresponding key in the 'status' dictionary
    else:
        # Here, we're comparing each character of the strings to find differences
        differences = [char1 for char1, char2 in zip(ref1_dict[key], ref2_dict[key]) if char1 != char2]  # Finds and stores differences in a list
        status[key].extend(differences)  # Adds those differences to the 'status' dictionary for that line number

# Write the results to a new text file
with open("ex_1_advanced_submit.txt", "w") as output:  # Opens a new file to write the results
    for key, value in status.items():  # Goes through each item in the 'status' dictionary
        output.write(f"{key} : {', '.join(value)}\n")  # Writes the status result for each line in the output file

