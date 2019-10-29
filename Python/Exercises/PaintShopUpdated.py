#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Charles      
Program Title: PaintShop
Description:  Allows you to use the program multiple times
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
#Paint Shop Calculator
#Program to calculate the number of gallons of paint required to paint a room, if provided the room dimensions

    def firstPrint():
    #Only need to print once
        print("Welcome to the Paint Shop!")
        print("This program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")
    
    firstPrint()


    def programsMass():

        import math

        square_feet_per_gallon = 150
        .0

        length = float(input("\nEnter the length of the room, in feet: "))
        width = float(input("Enter the width of the room, in feet: "))
        height = float(input("Enter the height of the room, in feet: "))

        totalArea = (length * height * 2) + (width * height * 2)


        gallons_of_paint = math.ceil(totalArea / square_feet_per_gallon)

    
        print("\nThe total wall area of your room is {0} square feet.".format(totalArea))
        print("You will need {0} gallon(s) of paint. \n\nHappy Painting!".format(gallons_of_paint))

    programsMass()

    YN = input("Do you want to calculate another room Yes/No.").upper()
    if YN == "YES":
        programsMass()
        YN = input("Do you want to calculate another room Yes/No.").upper()
        if YN == "YES":
            programsMass()
        else:
            print("Have a nice day!")
    else:
        print("Have a nice day!")
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()