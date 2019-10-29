#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Charles Pink 
Program Title:  Tax Calculator
Description:    It calculates tax
"""

#   -I need to assign variables too 
#   -Provinicial Withholding Tax 6% this is a float
#   -Federal Witholding Tax 25% this is a float
#   -Tax Deduction for Dependents 2% this is a float
#   -Amount of Dependants this is an integer
#   -Weekly Salary this is a 
#   
#   Welcome to the program message
#   I need them too imput the full amount of their weekly salary
#   I need them to input that amount of dependents they have
#   
#   Then I need too do the math
#   I need to know 6% of his weekly salary 0.06 x salary
#   I need to know 25% of his weekly salary 0.25 x salary
#   I need to know 2% of his weekly salary 0.02 x salary
#   Total witheld is ((0.25 x salary)(0.06 x salary))-(0.02 x Salary)
#   Total takehome is salary - total witheld 



def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!


#   -I need to assign variables too 

#   -Provinicial Withholding Tax 6% this is a float
    provTax = 0.06

#   -Federal Witholding Tax 25% this is a float
    fedTax = 0.25

#   -Tax Deduction for Dependents 2% this is a float
    depTaxDeduct = 0.02

#   -Amount of Dependants this is an integer
    amountOfDependants = 0

#   -Weekly Salary this is a float
    income = 0.0


#   Welcome to the program message
    print("Welcome to the loan calculator program! \n We will calculate your deductions for you! But first we need some informations \n")
#   I need them too imput the full amount of their weekly salary
    income = float(input("Please input the full amount of your salary you make per week: "))
#   I need them to input that amount of dependents they have
    amountOfDependants = int(input("Please input the amount of dependants you have: "))
    

#   Then I need too do the math
#   I need to know 6% of his weekly salary 0.06 x income

    provTaxWitheld = (provTax * income)
    print("\n\n\n Provincial Tax witheld: $" + "{0:.2f}".format(provTaxWitheld))

#   I need to know 25% of his weekly salary 0.25 x income

    fedTaxWitheld = (fedTax * income)
    print("Federal Tax witheld: $" + "{0:.2f}".format(fedTaxWitheld))

#   I need to know 2% of his weekly salary 0.02 x income

    dependantDeductition = (amountOfDependants * (depTaxDeduct * income))
    print("Your total dependant deduction for " + str(amountOfDependants) + " dependants : $" + "{0:.2f}".format(dependantDeductition))

#   Total witheld is 0.25 x salary + 0.06 x salary - 0.02 x Salary

    totalWitheld = ((fedTaxWitheld + provTaxWitheld) - dependantDeductition)
    print("Your total witheld: $" + "{0:.2f}".format(totalWitheld))

#   Total takehome is salary - total witheld 

    totalTakeHome = (income - totalWitheld)
    print("Your Total-Takehome pay: $" + "{0:.2f}".format(totalTakeHome))


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()