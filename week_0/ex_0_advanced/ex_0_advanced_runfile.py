while True:
    sequence = str(input("enter your DNA sequence: "))
    sequence = sequence.upper()
    valid = True
    for i in sequence:
        if i not in "ATGC":
            print("please enter a valid DNA sequence (ATGC)")
            valid = False
            break
    if valid:
        break
sequence_length = int(len(sequence))
nA = sequence.count("A")
nT = sequence.count("T")
nG = sequence.count("G")
nC = sequence.count("C")
GC_content = nG + nC
GC = ((GC_content)/sequence_length)
print("sequence length =" +str(sequence_length))
print("number of A: " +str(nA))
print("number of T: " +str(nT))
print("number of G: " +str(nG))
print("number of C: " +str(nC))
print("number of GC= " +str(GC_content), end="")
print(" with a proportion of" + str(GC))
if GC > 0.5:
    print(" Your sequence is rich in GC")
else:
    print(" Your sequence is poor in GC")