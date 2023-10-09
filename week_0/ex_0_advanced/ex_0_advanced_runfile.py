def analyze_dna_sequence():
    title = input("Please enter the title of the sequence: ")
    dna_sequence = input("Please enter the DNA sequence: ").upper()

    # Validate the DNA sequence
    if not set(dna_sequence).issubset({'A', 'C', 'G', 'T'}):
        print("Invalid DNA sequence. Only use the letters A, C, G, T.")
        return

    sequence_length = len(dna_sequence)
    adenine_count = dna_sequence.count('A')
    cytosine_count = dna_sequence.count('C')
    guanine_count = dna_sequence.count('G')
    thymine_count = dna_sequence.count('T')

    gc_content = ((guanine_count + cytosine_count) / sequence_length) * 100

    print(f"Sequence length: {sequence_length}")
    print(f"Number of adenine: {adenine_count}")
    print(f"Number of cytosine: {cytosine_count}")
    print(f"Number of guanine: {guanine_count}")
    print(f"Number of thymine: {thymine_count}")
    print(f"GC content: {gc_content:.2f}%")


# Run the function
analyze_dna_sequence()
