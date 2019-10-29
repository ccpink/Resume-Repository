#Don't forget to rename this file after copying the template
#for a new program!

"""
Student Name: Charles Pink   
Program Title:Bill Resturaunt
Description:A bill for a restaruant    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!



    #Need a variable bill
    
    #bill = 85
    #print("Your original bill amount is " + "{0:.0f}".format(bill))
    
    ##I need an input command to cover the bill variable in the program
    
    bill = input("Please input your original bill amount: ")

    #Need a variable tax
    tax = 0.15

    #Need a variable tip
    tip = .20

    #I need calculations 
    #Need tax totals and bill totals
    TaxedTotal = (float(bill)*tax)
    print('Your tax is', str(TaxedTotal))
    TipTotal = (float(bill)*tip)
    print("Your tip is", str(TipTotal))


    #I need the total calculations 

    total = TipTotal + TaxedTotal + float(bill)
    print("Your total is", str(total))
#I need too display the results of calculations

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()