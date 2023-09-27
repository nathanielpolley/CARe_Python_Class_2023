#YOUR CODE FOR EX_0 ADVANCED HERE
Floup = input("Put your DNA sequence here : \n")
DNA= Floup.upper()
LDNA = len(DNA)
A = DNA.count("A")
G = DNA.count("G")
C = DNA.count("C")
T = DNA.count("T")
GC = ((G+C)/LDNA)*100
print("The length of the DNA sequence is %d long.\nThere is %d Adenine, %d Guanine, %d Cytosine and %d Thymine.\nThe GC content is about %.2f" %(LDNA,A,G,C,T,GC))