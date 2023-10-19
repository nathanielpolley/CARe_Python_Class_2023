
import re  # Library for regular expressions (pattern searching and manipulation)
from fuzzywuzzy import fuzz  # Library for string similarity comparison


# Define a function to normalize a given reference
def normalize_reference(ref):

    # Remove all non-alphabetic characters and convert to lowercase
    ref = re.sub(r'[^a-zA-Z\s]', '', ref).lower()
    # Remove extra white spaces and return
    return ' '.join(ref.split())

# Define a function to compare references from two URLs
def compare_references():
    """
    Compares references from two predefined URLs and writes the comparison result to an output file.
    The references are considered similar if their normalized forms have a similarity ratio > 85.
    """

    # Read references from local files
    with open('references_1.txt', 'r') as f1, open('references_2.txt', 'r') as f2:
        references_1 = f1.read().splitlines()
        references_2 = f2.read().splitlines()

    # Open an output file to write the comparison results
    with open("ex_1_advanced_submit.txt", "w") as out_file:
        # Loop through each pair of references from the two files
        for i, (ref1, ref2) in enumerate(zip(references_1, references_2), start=1):
            # Normalize the references
            normalized_ref1 = normalize_reference(ref1)
            normalized_ref2 = normalize_reference(ref2)

            # Compare the similarity of the normalized references using a threshold of 85
            if fuzz.partial_ratio(normalized_ref1, normalized_ref2) > 85:
                # Write the "GOOD" status to the output file if references are similar
                out_file.write(f"{i} : GOOD\n")
            else:
                # Write the "DIVERGENT" status and the original references to the output file if they are divergent
                out_file.write(f"{i} : DIVERGENT\n")
                out_file.write(f"  In file 1: {ref1}\n")
                out_file.write(f"  In file 2: {ref2}\n")

# Entry point for the script
if __name__ == "__main__":
    # Call the function to compare references
    compare_references()
