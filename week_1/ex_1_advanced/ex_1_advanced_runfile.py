# Import necessary libraries
import requests  # Library for making HTTP requests
import re  # Library for regular expressions (pattern searching and manipulation)
from fuzzywuzzy import fuzz  # Library for string similarity comparison

# Define a function to fetch references from a given URL
def fetch_references_from_url(url):

    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Split the response text into lines and return as a list
    return response.text.splitlines()

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

    # Define the URLs containing references
    url1 = "https://raw.githubusercontent.com/mt93git/CARe_Python_Class_20231/d014e499f23a9939af4b08dd4fff32445a0248c3/week_1/ex_1_advanced/references_1.txt"
    url2 = "https://raw.githubusercontent.com/mt93git/CARe_Python_Class_20231/d014e499f23a9939af4b08dd4fff32445a0248c3/week_1/ex_1_advanced/references_2.txt"

    # Fetch the list of references from the URLs
    references_1 = fetch_references_from_url(url1)
    references_2 = fetch_references_from_url(url2)

    # Open an output file to write the comparison results
    with open("output.txt", "w") as out_file:
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
