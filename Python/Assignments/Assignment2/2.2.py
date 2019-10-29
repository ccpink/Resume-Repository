#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Charles Pink    
Program Title: Data Plan
Description: Calculates Data Plan costs
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Varaibles I need
    #I need one for the a variable for 200mb, 
    #over 200mb too 500mb, 
    #500 - 1gb and over 1gb
    #total at the end
    #User Input
    #firstRate = 20.00
    #secondRate = 0.105
    #thirdRate = 0.110
    #fourthRate = 118.00
    #totalCharge = 0.0
    #dataUsed = 0.
    #twoHundred = 200
    #fiveHundred = 500
    #oneThousand = 1000

    #Welcome Statement
    print("Welcome Erewhom Mobile Data Plans rate calculator!")
    #Function before the meat of the program
    def dataPlan(firstRate, secondRate, thirdRate, fourthRate, totalCharge, dataUsed, twoHundred, fiveHundred, oneThousand):
        #I need an input to get information from the user about how much data is going to be used
        dataUsed = float(input("Please enter the amount of data used in Mb's: "))
        #I'm going to need 4 different options for the 4 differernt plans
        
        if dataUsed <= twoHundred:
            totalCharge = firstRate
        elif dataUsed > twoHundred and dataUsed <= fiveHundred:
            totalCharge = dataUsed * secondRate
        elif dataUsed > fiveHundred and dataUsed <= oneThousand:
            totalCharge = dataUsed * thirdRate
        elif dataUsed > oneThousand:
            totalCharge = fourthRate
        #I need to display how much the plan would cost!
        print("Total charge is $" + "{0:.2f}".format(totalCharge))

    dataPlan(20.00, 0.105, 0.110, 118.00, 0.0, 0.0, 200, 500, 1000)


    #Ask if you want to repeat the program!
    YN = input("Do you want to calculate another room Yes/No.").upper()
    if YN == "YES":
        dataPlan(20.00, 0.105, 0.110, 118.00, 0.0, 0.0, 200, 500, 1000)
        YN = input("Do you want to calculate another room Yes/No.").upper()
        if YN == "YES":
            dataPlan(20.00, 0.105, 0.110, 118.00, 0.0, 0.0, 200, 500, 1000)
        else:
            print("Have a nice day!")
    else:
        print("Have a nice day!")

    
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()