"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #We need an input for,
    #Tons and we need a variable attached to it tons
    tons = int(input("Please input the number of tons: "))
    print(tons)
    #Stone and we need a variable attached to it stone
    stone = int(input("Please input the number of stones: "))
    print(stone)
    #Pounds and we need a variable attached to it pounds
    pounds = int(input("Please input the number of pounds: "))
    print(pounds)
    #Ounces and we need a variable attached to it ounces
    ounces = int(input("Please input a number of ounces: "))
    #We need to convert all of these too total ounces and we need a var attached totalOunces
    #Math for this is total ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
    totalOunces = (35840 * tons + 224 * stone + 16 * pounds + ounces)
    #we need to conver total ounces to total kilos and a var for it totalKilos
    #Math for this is total kilos = total ounces / 35.27
    
    metricTons = (totalOunces / 35273.96)
    #print(metricTons) use to test variable that it outputs correctly
    totalKilos = (totalOunces / 35.27396) - (int(metricTons))*1000
    #print(totalKilos) use to test variable that it outputs correctly
    totalGrams = ((totalOunces / 0.035274) - (int(metricTons))*1000000) - (int(totalKilos)*1000)
    #print(totalGrams) use to test variable that it outputs correctly
    #Output in clear letters for the person viewing the information
    print("The metric weight is", "{0:.0f}".format(metricTons), " metric tons,", "{0:.0f}".format(totalKilos),"kilos. and", "{0:.1f}".format(totalGrams), "grams.")
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()