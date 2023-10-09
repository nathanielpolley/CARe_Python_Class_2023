# import math
DNASeq = input("Enter the  DNA Sequence: ")
DNASeq = DNASeq.upper()
allowedLetters = ['A', 'C', 'G', 'T']
if any(words in DNASeq for words in allowedLetters):
    DNAlength = len(DNASeq)
    Adenine_count = DNASeq.count('A')
    Cytosine_count = DNASeq.count('C')
    Guanine_count = DNASeq.count('G')
    Thymine_count = DNASeq.count('T')
    addition = Cytosine_count + Guanine_count
    Division = addition / DNAlength
    percentage = Division * 100
    print(f"The DNA sequence length: {DNAlength}")
    print(f"The number of adenine bases: {Adenine_count}")
    print(f"The number of cytosine bases: {Cytosine_count}")
    print(f"The number of guanine bases: {Guanine_count}")
    print(f"The number of thymine bases: {Thymine_count}")
    print(f"The GC content: {percentage}")
else:
     print("the DNA sequence is invalid")