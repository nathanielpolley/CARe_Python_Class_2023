#YOUR CODE FOR EX_0 ADVANCED HERE



dna = (input("Enter a DNA sequence (A, C, G, T only): ")).upper()
def s_len (dna):
    sequence_length = len(dna)
    return sequence_length


#Now we need to count

def count_dna (dna):
    A_nb = C_nb = G_nb = T_nb = 0
    for base in dna:
        if base == 'A':
            A_nb += 1
        elif base == 'C':
            C_nb += 1
        elif base == 'G':
            G_nb += 1
        elif base == 'T':
            T_nb += 1
        else:
            # Error: Invalid base found
            print("Error: this is not a dna sequence !")
    return [A_nb, C_nb, G_nb, T_nb]

# Calculate GC content
gc_content = (count_dna(dna)[1]+count_dna (dna)[2]) /  s_len(dna) * 100


print("Sequence Length:", s_len(dna))
print("A Count:", count_dna(dna)[0])
print("C Count:", count_dna(dna)[1])
print("G Count:", count_dna(dna)[2])
print("T Count:", count_dna(dna)[3])
print("GC Content:", gc_content, '%')

#sequence len and count
s_len(dna)
count_dna(dna)
