"""
Student Name:Charles Pink       
Program Title:Loan Calculator
Description:Calculates Loan payments    
"""

# Variables Needed 
# loanAmount float()
# interestRate float()
# convertedinterest float()
# numberOfYears int()
# weeklyPayment float()
#
# I need to promt the user for their loan amount
# I need to prompt the user for their interest rate
# I need to prompt the user for the number of years
# I need to caluculate the weekly payment amount  (convertedInterest = interestRate / 5200)    and  ((i)/(1-(1+i)^-52n))*A  
# I need present the information to the user of what their weekly payment will be

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    
    #Welcome Statement
    print("Hello welcome to the loan calculator") 
    #Variables the amount of the loan, the interest rate of the loan, and the number of years they want to pay it back.
    loanAmount = float(input("Please enter the amount of the loan: "))
    interestRate = float(input("Please enter the interest rate of the loan: "))
    numberOfYears = int(input("Please enter the number of years you wish to be paying it back: "))


    #Doing the calculation on the interest rate
    convertedInterest = (interestRate/5200)
    #making the months of the years before using the calculation 
    months = numberOfYears * 52
    #The final calculation (interest / (1 - (1 + interest)** months) * loanAmount
    weeklyPayment = (convertedInterest / (1 - (1 + convertedInterest)** -months) * loanAmount)
      
    #Print the amount they need to pay per week for the amount of years specified.
    print("Your weekly payment is: ${0:.2f}".format(weeklyPayment))

 



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()