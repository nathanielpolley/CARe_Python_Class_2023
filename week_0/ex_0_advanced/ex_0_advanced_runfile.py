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
sequence_lenght = int(len(sequence))
nA = 0
nT = 0
nG = 0
nC = 0
for i in sequence:
    if i == "A":
        nA +=1
    else:
        pass
    if i == "T":
        nT +=1
    else:
        pass
    if i == "G":
        nG +=1
    else:
        pass
    if i == "C":
        nC +=1
GC_content = nG + nC
GC = ((GC_content)/sequence_lenght)
print("sequence lenght =" +str(sequence_lenght))
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