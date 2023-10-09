# import math
DNASeq = input("Enter the  DNA Sequence: ")
DNASeq = DNASeq.upper()
allowedLetters = ['A', 'C', 'G', 'T']
DNAlength = len("DNASeq")
Adenin_count = DNASeq.count('A')
Cytosine_count = DNASeq.count('C')
Guanine_count = DNASeq.count('G')
Thymine_count = DNASeq.count('T')
GC_content = DNASeq.count('GC')
if any(words in DNASeq for words in allowedLetters):
    print(f"The DNA sequence length: {DNAlength}")
    print(f"The number of adenine bases: {Adenin_count}")
    print(f"The number of cytosine bases: {Cytosine_count}")
    print(f"The number of guanine bases: {Guanine_count}")
    print(f"The number of thymine bases: {Thymine_count}")
    print(f"The GC content: {GC_content}")
else:
     print("the DNA sequence is invalid")