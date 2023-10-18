def analyze_dna_sequence(sequence):
    sequence = sequence.upper()  # Convert the input to uppercase to handle both upper and lower case characters

    # Check if the sequence contains only valid DNA bases
    if set(sequence) - set("ACTG"):
        print("Invalid DNA sequence. Please enter a sequence containing only A, C, G, and T.")
        return

    # Calculate and display sequence length
    sequence_length = len(sequence)
    print(f"Sequence Length: {sequence_length} base pairs")

    # Calculate and display the counts of each base (A, C, G, and T)
    counts = {
        'A': sequence.count('A'),
        'C': sequence.count('C'),
        'G': sequence.count('G'),
        'T': sequence.count('T')
    }
    print(f"A Count: {counts['A']}")
    print(f"C Count: {counts['C']}")
    print(f"G Count: {counts['G']}")
    print(f"T Count: {counts['T']}")

    # Calculate and display GC content
    gc_content = (counts['G'] + counts['C']) / sequence_length * 100
    print(f"GC Content: {gc_content:.2f}%")

if __name__ == "__main__":
    # Prompt the user to input a DNA sequence
    dna_sequence = input("Enter a DNA sequence: ")
    analyze_dna_sequence(dna_sequence)