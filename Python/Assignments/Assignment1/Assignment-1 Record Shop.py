"""
Student Name:Charles Pink   
Program Title:Weight Conversions
Description:Converts weights into different weights    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #This is sales tax
    salesTax = 0.14
    #This is delivery rate
    deliveryRate = 15   


    print("Hipster's Local Vinyl Records - Customer Order Details")

    #Customers Name Input
    name = input("Enter the customer's name: ")
    #Customers Name Check to see if it was right?
    print("The customers name is", name)
    yesOrNo = input("Is this correct? (Yes)(No)")
    if yesOrNo =='Yes':
        print("Moving on")
    else:
        name = input("Please input customer's name again.: ")
        print("Moving on")

#Distance in Kilometers Input
    distance = input("Please input the distance in kilometers: ")
    print("The distance is", distance, "kilometers")
#Distance Input Check to see if they input correctly
    yesOrNo = input("Is this correct? (Yes)(No)")
    if yesOrNo =='Yes':
        print("Moving on")
    else:
        distance = input("Please input the distance in kilometers again.: ")
        print("Moving on")

#Enter cost of records
    recordCosts = input("Please input the cost of the records bought: ")
    print("The cost of records are $" + recordCosts)
#Distance Input Check to see if they input correctly
    yesOrNo = input("Is this correct? (Yes)(No)")
    if yesOrNo =='Yes':
        print("Moving on")
    else:
        recordCosts = input("Please input the cost of the records bought again.: ")
        print("Moving on")





    #Details about the puchase / Persons name.
    print("\n \nPurchase Summary for", name, ".")

    #Calculations for delivery cost.
    #Does delivery have tax attached?
    costOfDistance = (float(distance) * 15)
    #Delivery Cost.
    print("The cost of delivery will be $" + str("{0:.2f}".format(costOfDistance)))
    #Calculations for purchase cost.
    tax = (float(recordCosts)*salesTax) 
    purchaseCost = (tax + float(recordCosts))
    #Purchase Cost.
    print("The cost of purchase is $" + "{0:.2f}".format(purchaseCost))
    #Total tax. 
    print("The total tax is $" + ("{0:.2f}".format(tax)))
    #Calculations for total cost.
    total = (purchaseCost + costOfDistance)
    #Total Cost.
    print("The total cost is $" + "{0:.2f}".format(total))




    #Your code ends on the line above
#Do not change any of the code below!
if __name__ == "__main__":
    main()