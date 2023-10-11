#YOUR CODE FOR EX_0 ADVANCED HERE
#GATCGATCGATCGATCGATCGATCGATCGATCGATC
import math

InputSequence = input("Please enter the DNA Sequence.")
InputSequence = InputSequence.upper()
#print(InputSequence.upper())
SequenceCheck = ["A", "G", "C", "T"]

Validation = [i in SequenceCheck for i in InputSequence]
#print(all(Validation))

if not all(Validation) == True:
    print("Please ensure your DNA sequence only contains A,C,T,G")

else:
    print("Thank you!")
    Length = len(InputSequence)
    print("The length of the sequence is ", Length)

    from collections import Counter
    print("The Nucleotide Base numbers are ", Counter(InputSequence))
    c = Counter(InputSequence)

    GC = ((c["G"] + c["C"]) / Length)*100
    print("The GC Content is ", round(GC, 2), "%")
