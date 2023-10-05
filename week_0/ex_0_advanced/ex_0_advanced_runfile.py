#YOUR CODE FOR EX_0 ADVANCED HERE

DNA_Seq = input("Enter your DNA Sequence Here: ")


#find length of given DNA Sequence
counter = 0
for i in DNA_Seq:
    counter += 1
    length = len(DNA_Seq)
    print(length)


#find number of adenines
counterA = 0
for i in DNA_Seq:
    if i == 'A':
        counterA += 1
print(counterA)
print("Adenine found")

#find number of guanines
counterG = 0
for i in DNA_Seq:
    if i == 'G':
        counterG += 1
print(counterG)
print("Guanine found!")

#find number of thymines
counterT = 0
for i in DNA_Seq:
    if i == 'T':
        counterT += 1
print(counterT)
print("Thymine found!")

#find number of cytosines
counterC = 0
for i in DNA_Seq:
    if i == 'C':
        counterC += 1
print(counterC)
print("Cytosine found!")

#find GC content


x = counterC
y = counterG
def totalGC(x,y):
    total = x + y
    percentage = total/100
    ans = percentage
    return ans


