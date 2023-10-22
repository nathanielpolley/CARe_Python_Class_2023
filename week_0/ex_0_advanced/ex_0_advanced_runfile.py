
#GTCGATAACTAGCTAACGGCT

def DNA_sequence_analysis(seq):

    count_A = seq.count("A")
    count_C = seq.count("C")
    count_G = seq.count("G")
    count_T = seq.count("T")
    GC_tot = count_G + count_C
    GC_content = (GC_tot/len(seq)) * 100
    print("Adenine count: ",count_A)
    print("Cytosine count: ",count_C)
    print("Guanine count: ",count_G)
    print("Thymine count: ",count_T)
    print("GC content is: ", GC_content)


seq = str(input("Enter your DNA sequence: "))
if any(x not in ["A","C","G","T"] for x in seq):
    print("Please enter a DNA sequence")
else:
    length = len(seq)

    print("DNA sequence length: ",length)

    print(DNA_sequence_analysis(seq))