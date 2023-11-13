dna_sequence=input('enter the DNA sequence:')
#check if DNA sequence and length
dna_sequence=dna_sequence.upper()
length=len(dna_sequence)
if(dna_sequence.count("A")+dna_sequence.count("T")+dna_sequence.count("C")+dna_sequence.count("G"))==length:
    print('valid sequence')
    print("The sequence length is " + str(length) + " nucleotides long")
    print("The number of adenosine is:", dna_sequence.count("A"))
    print("The number of guanine is:", dna_sequence.count("G"))
    print("The number of thymidine is:", dna_sequence.count("T"))
    print("The number of cytosine is:", dna_sequence.count("C"))
    GC_content=((dna_sequence.count("G")+dna_sequence.count("C"))/length)*100
    print('The sequence contains ' + str(GC_content) + '% of GC')

else:
    print('invalid sequence, please enter a DNA sequence')





