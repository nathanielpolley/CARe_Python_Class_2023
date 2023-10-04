#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math
def calculate_growth_rate() :
    try :
        C0= int(input("Enter initial count : "))
        Cf = int(input("Enter final count : "))
        T = int(input("Enter time : "))

        if (T <= 0) and (C0 > Cf) :
            print("only positive numbers are allowed and initial value must be less than the final one")
        else :
            growth_rate = (math.log(Cf)-math.log(C0))/T
            print(f"Growth rate is : '{growth_rate}")

    except ValueError :
            print("Invalid input. You need a number of cells > or = to 0")


calculate_growth_rate()





