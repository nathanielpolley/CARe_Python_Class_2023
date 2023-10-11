#YOUR CODE FOR EX_0 ADVANCED HERE
#GATCGATCGATCGATCGATCGATCGATCGATCGATC
import math

InputSequence = input("Please enter the DNA Sequence.")
SequenceCheck = ["A", "G", "C", "T"]

Validation = [i in SequenceCheck for i in InputSequence]
#print(all(Validation))

if not all(Validation) == True:
    print("Please ensure your DNA sequence only contains A,C,T,G")

else:
    InputSequence.upper()
    print("Thank you!")
    Length = len(InputSequence)
    print("The length of the sequence is ", Length)
    A = InputSequence.count("A")
    T = InputSequence.count("T")
    G = InputSequence.count("G")
    C = InputSequence.count("C")
    print("The amount of Adenine is ", A)
    print("The amount of Tyrosine is ", T)
    print("The amount of Guanine is ", G)
    print("The amount of Cytosine is ", C)
    GCContent = ((G+C) / (G+C+T+A))*100
    print("The GC Content is ", round(GCContent, 2), "%")
