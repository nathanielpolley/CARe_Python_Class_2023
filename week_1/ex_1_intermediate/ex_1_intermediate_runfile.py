#YOUR CODE FOR EX_1 INTERMEDIATE HERE
# User input

import pandas as pd

MicrobialSpecies = ["Archaea", "Bacteria", "Fungi", "Protists", "Virus"]
MicrobialCount = {"Archaea": 3, "Bacteria": 8, "Fungi": 12, "Protists": 11, "Virus": 12}

data = {
    'Microbial Species': ["Archaea", "Bacteria", "Fungi", "Protists", "Virus"],
    'Microbial Count': [3, 8, 12, 11, 12]

}

df = pd.DataFrame(data)

#prints the dictionary.
print("DataFrame created from a dictionary:")
print(df)
print("\n")

#counts the number of samples in the dictionary.
final = 0

for total in MicrobialCount:
    if isinstance(total, int):
        final += total

print(total)





