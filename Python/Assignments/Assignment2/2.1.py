#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Charles   
Program Title: Landscape Calculator
Description:  Finds the price of a landscaping job
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Variables
    #Base Labour Charge
    #baseLabour = 1000.00
    #500$ base for surface 
    #surchargeFee = 500.00
    #Bentgrass cost 0.02$
    #bentGrass = 0.02
    #fescue grass cost 0.05$
    #fescueGrass = 0.05
    #campus grass cost 0.01$
    #campusGrass = 0.01
    #Tree cost 100$
    #treeCost = 100
    #number of trees
    #numOfTrees = 0
    #grass type
    #typeOfGrass = ""
    #plot length by feet
    #plotLength = 0.0
    #plot width
    #plotDepth = 0.0
    #House number 
    #houseNum = 0
    #plotSize
    #plotSize = 0.0
    #End Total variable
    #endTotal = 0.00
    #cost of their trees
    #priceOfTrees = 0
    #surcharge fee if larger than 5000
    #surchargeArea = 5000

    #Welcome message
    print("Hello welcome to the landscape companies calculator please input your data below!")
    #I need them to input their house number

    def Finale(baseLabour, surchargeFee, bentGrass, fescueGrass, campusGrass, treeCost, numOfTrees, typeOfGrass, plotDepth, plotWidth, houseNum, plotSize, endTotal, priceOfTrees, surchargeArea):

        houseNum = int(input("Please input your house number: "))
        #I need them to input their grass type
        typeOfGrass = input("Please input your type of grass! (fescue, bentgrass, campus): ").lower()
        #I need them to input their plot length and width
        plotDepth = float(input("Please input your plots width: "))
        plotLength = float(input("Please input your plots depth: "))
        #I need them to enter the number of trees on their property turn into an int
        numOfTrees = int(input("Please input the number of trees: "))



        #Calculate plot Size
        plotSize = plotDepth * plotLength
        #If fescue calculate fescue price
        #Calculation is the cost of grass times the size of the plot
        if typeOfGrass == "fescue":
            endTotal = fescueGrass * plotSize
        #If bentgrass calculate bentgrass price
        #Calculation is the cost of grass times the size of the plot
        elif typeOfGrass == "bentgrass":
            endTotal = bentGrass * plotSize
        #If campus grass calculate price for campus
        #Calculation is the cost of grass times the size of the plot
        elif typeOfGrass == "campus":
            endTotal = campusGrass * plotSize
        #Calc the price of trees
        priceOfTrees = numOfTrees * treeCost
        #Check if there is a large enough area to apply a fee of 500$
        #If not pass over and just finish the calculation. 
        if plotSize > surchargeArea:
            endTotal = endTotal + surchargeFee    
        #Finish Calculating the end Total
        endTotal = endTotal + priceOfTrees + baseLabour
        #Print the end statement. 
        print("Total cost for house", str(houseNum), "is: $" + "{0:.2f}".format(endTotal))   

    Finale(1000.00, 500.00, 0.02, 0.05, 0.01, 100, 0, "", 0.0, 0.0, 0, 0.0, 0.00, 0, 5000)     
        

    YN = input("Do you want to calculate another room Yes/No.").upper()
    if YN == "YES":
        Finale(1000.00, 500.00, 0.02, 0.05, 0.01, 100, 0, "", 0.0, 0.0, 0, 0.0, 0.00, 0, 5000)
        YN = input("Do you want to calculate another room Yes/No.").upper()
        if YN == "YES":
            Finale(1000.00, 500.00, 0.02, 0.05, 0.01, 100, 0, "", 0.0, 0.0, 0, 0.0, 0.00, 0, 5000)
        else:
            print("Have a nice day!")
    else:
        print("Have a nice day!")
    #Your code ends on the line above


#Do not change any of the code below!
if __name__ == "__main__":
    main()