#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    
    #Welcome Messages
    print("Hello welcome to the airport.")
    #Input for the weight
    luggageWeight = float(input("Please put in the weight of your luggage in pounds: "))
    #If Statement to see if ts more than 50lb #If true give them a surcharge of 25$
    print("Are you sure your luggage weighs", "{0}".format(luggageWeight))
    if luggageWeight > 50: 
        print("You will be charged an additional 25$ as a surcharge")
    #End message saying goodbye or thanks for using the airplanes services
    print("Please have a good day and a nice flight.")
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()