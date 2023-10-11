#YOUR CODE FOR EX_0 ADVANCED HERE

dna = (input("Enter a DNA sequence (A, C, G, T only): ")).upper()
def s_len (dna):
    sequence_length = len(dna)
    return sequence_length

#Now we need to count

def count_dna (dna):
    for base in dna:
        if (base != 'A' and base !='C'and base != 'G' and base != 'T'):
            # Error: Invalid base found
            print("Error: this is not a dna sequence !")
            return()
    return [dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')]

# Calculate GC content
gc_content = (count_dna(dna)[1]+count_dna (dna)[2]) /  s_len(dna) * 100


print("Sequence Length:", s_len(dna))
print("A Count:", count_dna(dna)[0])
print("C Count:", count_dna(dna)[1])
print("G Count:", count_dna(dna)[2])
print("T Count:", count_dna(dna)[3])
print("GC Content:", gc_content, '%')

#done

