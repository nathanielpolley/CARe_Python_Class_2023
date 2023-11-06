#YOUR CODE FOR EX_0 ADVANCED HERE

DNA_Seq = input.upper("ENTER YOUR DNA SEQUENCE HERE: ") or input.lower("enter your dna sequence here")
if i in DNA_Seq != 'A' or 'T' or 'C' or 'G' or 'a' or 't' or 'c' or'g':
    print("Please enter a valid sequence. Try again!") #to ensure upper + lowercase is acceptable



#Alternative to using multiple for lopps!!!! so great thanks!
from collections import Counter
counter = Counter(DNA_Seq)
counter['A'], counter['T'], counter['C'], counter['G'] #gives me the exact # of specific bases!


#OR
adenine = counter['A']
thymine = counter['T']
guanine = counter['G']
cytosine = counter['C']

print(adenine, thymine, guanine, cytosine)
#find GC content


x = counterC
y = counterG
def totalGC(x,y):
    total = x + y
    percentage = total/100
    ans = percentage
    return ans


