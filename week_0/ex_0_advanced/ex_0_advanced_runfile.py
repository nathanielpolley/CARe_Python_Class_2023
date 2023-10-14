#YOUR CODE FOR EX_0 ADVANCED HERE

import sys
print(sys.version)

def Sequence() :
    DNA_seq = str(input("Enter DNA sequence :"))
    DNA = (DNA_seq.upper())
    DNA_letters = "ATGC"
    count = 0
    for letter in DNA :
        if DNA_letters.find(letter) == -1:
            count = count + 1
    if count > 0:
        print("invalid input, sequence could only contain the following letters (a,t,c,g)")
    else :
        print("The sequence lenght is : " + str(len(DNA)))
        print("The number of A is :" + str(DNA.count("A")))
        print("The number of T is :" + str(DNA.count("T")))
        print("The number of G is :" + str(DNA.count("G")))
        print("The number of C is :" + str(DNA.count("C")))
        print("The number of GC is :" + str(DNA.count("GC")))
Sequence()












