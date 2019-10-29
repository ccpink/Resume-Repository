#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Charles Pink   
Program Title: Grade System Calculator 
Description: Helps in grading   
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    #I need variables for each letter grade I need a variable for + / -  
    letterA = "A"
    letterB = "B"
    letterC = "C"
    letterD = "D"
    letterF = "E"
    plus = 0.3
    minus = -0.3
    void = ""
    gradeA = 4.0
    gradeB = 3.0
    gradeC = 2.0
    gradeD = 1.0
    gradeF = 0.0
    #I need a variable for the intputs by the user so the grade modifier and the grade itself.
    studentGrade =""
    gradeMod =""
    #opening messages
    print("Welcome to the Grade Point Calculator \n Thank you for using our services \n \
        \n Valid letter grades that can be entered: A, B, C, D, F. \n Valid grade modifiers are +, - or nothing \
         \n All letter grades except F can include a + or - symbol. \n Calculated grade point value cannot exceet 4.0. \n ")
    #I need to make sure the inputs are valid 
    studentGrade = input("Please enter a letter grade : ").upper()
    gradeMod = input("Please enter a modifier (+, - or nothing) : ")
    #I need to check what the letter grade is
    if studentGrade == letterA:
        total = gradeA
        if gradeMod == "-":
            total = gradeA + minus
            print("The Numeric Value is :", "{0:.1f}".format(total))
        elif gradeMod == "+":
            total = gradeA + plus
            print("The Numeric Value is :", "{0:.1f}".format(total))
        elif gradeMod == void:
            print("The Numeric Value is :", "{0:.1f}".format(total))
        else:
            print("You entered an invalid grade modifications, we will do the calculations with the base stats!")
            print("The Numeric Value is :", "{0:.1f}".format(total))
    elif studentGrade == letterB:
        total = gradeB 
        if gradeMod == "-":
            total = gradeB + minus
            print("The Numeric Value is :", "{0:.1f}".format(total))
        elif gradeMod == "+":
            total = gradeB + plus
            print("The Numeric Value is :", "{0:.1f}".format(total))
        elif gradeMod == void:
            print("The Numeric Value is :", "{0:.1f}".format(total))
        else:
            print("You entered an invalid grade modifications, we will do the calculations with the base stats!")
            print("The Numeric Value is :", "{0:.1f}".format(total))
    elif studentGrade == letterC:
        total = gradeC
        if gradeMod == "-":
            total = gradeC + minus
            print("The Numeric Value is :", "{0:.1f}".format(total))
        elif gradeMod == "+":
            total = gradeC + plus
            print("The Numeric Value is :", "{0:.1f}".format(total))
        elif gradeMod == void:
            print("The Numeric Value is :", "{0:.1f}".format(total))
        else:
            print("You entered an invalid grade modifications, we will do the calculations with the base stats!")
            print("The Numeric Value is :", "{0:.1f}".format(total))
    elif studentGrade == letterD:
        total = gradeD 
        if gradeMod == "-":
            total = gradeD + minus
            print("The Numeric Value is :", "{0:.1f}".format(total))
        elif gradeMod == "+":
            total = gradeD + plus
            print("The Numeric Value is :", "{0:.1f}".format(total))
        elif gradeMod == void:
            print("The Numeric Value is :", "{0:.1f}".format(total))
        else:
            print("You entered an invalid grade modifications, we will do the calculations with the base stats!")
            print("The Numeric Value is :", "{0:.1f}".format(total))
    elif studentGrade == letterF:
        total = gradeF
        if gradeMod == "-":
            total = gradeF + minus
            print("The Numeric Value is :", "{0:.1f}".format(total))
        elif gradeMod == "+":
            total = gradeF + plus
            print("The Numeric Value is :", "{0:.1f}".format(total))
        elif gradeMod == void:
            print("The Numeric Value is :", "{0:.1f}".format(total))
        else:
            print("You entered an invalid grade modifications, we will do the calculations with the base stats!")
            print("The Numeric Value is :", "{0:.1f}".format(total))
    else : 
        print("You entered an invalid letter grade.")
#I need to check against + or - 
# #I need a ending message 
    #Your code ends on the line above
#Do not change any of the code below!
if __name__ == "__main__":
    main()