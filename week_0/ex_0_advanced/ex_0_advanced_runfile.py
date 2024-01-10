# Matias Medina Tanco: EX_0 ADVANCED

# Example 10nt sequence: tgcagacaga
# Example 100nt sequence: tgtaagtctccacaagtccccgattctctgggaaccataaattaaattgcagttggaaagatcatagttggcgtatagactcagcctacggcgacgtacc

while True:
    # Ask for sequence
    sequence = input("Enter your DNA sequence: ")

    # List of allowed nucleotides
    nucleotides = "ACGTacgt"

    # Check that sequence is valid (only contains allowed nucleotides)
    check = all(ch in nucleotides for ch in sequence)

    if check == True:

        # Calculate sequence length, nucleotide counts and CG content
        Length = len(sequence)
        countA = sequence.count('A') + sequence.count('a')
        countC = sequence.count('C') + sequence.count('c')
        countG = sequence.count('G') + sequence.count('g')
        countT = sequence.count('T') + sequence.count('t')
        contentCG = (countC + countG) / Length * 100

        # Print out results
        print("The sequence is ", Length, "nucleotides long.")
        print("It has:")
        print(countA, " adenine(s)")
        print(countC, " cytosine(s)")
        print(countG, " guanine(s)")
        print(countT, " thymine(s)")
        print("It also has a GC content of ", contentCG, "%")

        #get out of loop and end program
        break

    else:
        print("Please give a valid DNA sequence")