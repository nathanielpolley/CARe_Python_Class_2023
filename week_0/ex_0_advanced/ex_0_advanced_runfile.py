dna_sequence = str(input('Add the DNA sequence here: '))
dna_sequence = dna_sequence.upper()
if all(nucleotides in "ACTG" for nucleotides in dna_sequence):
    print("DNA sequence valid.")
else:
    print("Give me only nucleotides in a DNA structure!")

print(len(dna_sequence))
print("Number of Adenosine: ", dna_sequence.count("A"))
print("Number of Cytosine: ", dna_sequence.count("C"))
print("Number of Guanine: ", dna_sequence.count("G"))
print("Number of Thymine: ", dna_sequence.count("T"))
print("Number of GC: ", dna_sequence.count("GC"))