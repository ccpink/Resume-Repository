#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Charles   
Program Title:  Auto Insurance
Description:  Auto Insurance Calculator.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

#Variables
#Male, Female, Percent Increase for male and female rates in the three brackets, Multiplication Rate, Age Ranges, Inputd customer, age/price of vehicle/male or female/, Total, 
#male, \female,  \mRate1,| mRate2, |mRate3,| fRate1,| fRate2,| fRate3,| multiplicationRate,|age1,|age2,| age3,| customerAge,|customerSex, |vehicleprice, | endTotal
#"MALE",\"FEMALE",\ 0.25,| 0.17 , |0.1,    | 0.2,   |0.15,  |0.1,     |12,                 |25, |40,   |70,   |0,           |"",         |0.0,           |0.0
    print("Welcome to the Aut Insurance Calculator")
    def autoInsurance(male, female, mRate1, mRate2, mRate3, fRate1, fRate2, fRate3, multiplicationRate, age1, age2, age3, age0, customerAge, customerSex, vehicleprice, endTotal):
        #I need an input for if they are male or female, their age and the purchase price of their vehicle
        customerSex = input("Are you 'Male' or 'Female': ").upper()
        customerAge = int(input("Please enter your age: "))
        vehicleprice = float(input("Please enter the purchase price of your vehicle: "))
        #I need to check the results of customer age 
        if customerSex == female:
            #Then I need to check their age in response to their sex
            if customerAge >= age0 and customerAge < age1: 
                endTotal = vehicleprice * fRate1 / multiplicationRate
            elif customerAge >= age1 and customerAge < age2:
                endTotal = vehicleprice * fRate2 / multiplicationRate   
            elif customerAge >= age2 and customerAge < age3:
                endTotal = vehicleprice * fRate3 / multiplicationRate
        #I need to do the same thing with the male side but plug in slightly different values for their rates.
        elif customerSex == male:
            if customerAge >= age0 and customerAge < age1: 
                endTotal = vehicleprice * mRate1 / multiplicationRate   
            elif customerAge >= age1 and customerAge < age2:
                endTotal = vehicleprice * mRate2 / multiplicationRate    
            elif customerAge >= age2 and customerAge < age3:
                endTotal = vehicleprice * mRate3 / multiplicationRate
        else:
            pass

        if endTotal > 0:    
            print("Your monthly insurance will be $" + "{0:.2f}".format(endTotal))
    autoInsurance("MALE", "FEMALE", 0.25, 0.17 , 0.1, 0.2, 0.15, 0.1, 12, 25, 40, 70, 15, 0, "", 0.0, 0.0)
       
    

    YN = input("Do you want to calculate another room Yes/No.").upper()
    if YN == "YES":
        autoInsurance("MALE", "FEMALE", 0.25, 0.17 , 0.1, 0.2, 0.15, 0.1, 12, 25, 40, 70, 15, 0, "", 0.0, 0.0)
        YN = input("Do you want to calculate another room Yes/No.").upper()
        if YN == "YES":
            autoInsurance("MALE", "FEMALE", 0.25, 0.17 , 0.1, 0.2, 0.15, 0.1, 12, 25, 40, 70, 15, 0, "", 0.0, 0.0)
        else:
            print("Have a nice day!")
    else:
        print("Have a nice day!")
    #Your code ends on the line above
#Do not change any of the code below!
if __name__ == "__main__":
    total = main()


  