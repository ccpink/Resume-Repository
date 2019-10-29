#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

#I need to create variables for total for order, Country and Provinces as well as taxes for the provinces

    originalPrice = 0.0
    country = ""
    province = ""
    alb = "alberta"
    nS = "nova scotia"
    ont = "ontario"
    newB = "new brunswick"
    albTax = 0.05
    ontTax = 0.15
    newBTax = 0.15
    novaScotiatax = 0.15
    otherPrv = 0.11
    endtotal = 0.0
    canada = "canada"
    

#Welcome message
    print("Hello welcome to the Online Store checkout.")

#Ask user for their country and original price
    originalPrice = float(input("What is your current total before taxes.: "))
    country = input("Please input your country in which you live!: ")
    endtotal = originalPrice
#If canada 
    if canada == country.lower():
        #if so they have taxes
        print("You have taxes!")
#Ask what province 
        province = input("Please input your province: ").lower()
        if province == alb:
            endtotal = (originalPrice * albTax + originalPrice)
        elif province == nS:
            endtotal  = (originalPrice * novaScotiatax + originalPrice)
        elif province == ont:
            endtotall = (originalPrice + ontTax + originalPrice)
        elif province == newB:
            endtotal = (originalPrice + newBTax + originalPrice)
                
        else: endtotal = (originalPrice * otherPrv + originalPrice) 
        
#Else print there are no taxes
    else:
        print("You have no taxes")
    
    print("Your total is ""{0:.2f}".format(endtotal))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()