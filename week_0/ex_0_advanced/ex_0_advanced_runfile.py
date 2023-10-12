#
import math
DNAseq = input("Enter DNA sequence")
DNAseq = DNAseq.upper()

if any(words not in "ATGC" for words in DNAseq):
    print("wrong sequence")
else:
    lenght = len(DNAseq)
    A = DNAseq.count('A')
    C = DNAseq.count('C')
    G = DNAseq.count('G')
    T = DNAseq.count('T')
    GC = G + C
    GCratio = GC / lenght
    GCpercent = GCratio * 100
    print(f"The lenght is: {lenght}")
    print(f"adenine is: {A}")
    print(f"cytosine is: {C}")
    print(f"guanine is: {G}")
    print(f"thymine is: {T}")
    print(f"GC content is: {GCpercent}")

