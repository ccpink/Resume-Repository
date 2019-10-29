#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Charles Pink    
Program Title: Data Plan
Description: Calculates Data Plan costs
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
   
   #For loop
    for myCounter in range(1, 6):

        name = input(" Hello please enter your name: ")
        if myCounter == 1: 
            name1 = name 
        elif myCounter == 2:
            name2 = name
        elif myCounter == 3:
            name3 = name   
        elif myCounter == 4:
            name4= name
        elif myCounter == 5:
            name5 = name
    
    print("Hello", name1, name2, name3, name4, name5)
    #Your code ends on the line above
    numberFalse = True
    while numberFalse == True:
        Uservalue = input("Enter one alpha letter : ").upper()
        if Uservalue.isalpha() == True and len(Uservalue) == 1:
            print("Good Job")
            numberFalse = False
        else:
            print("You can't read try again")
  
#Do not change any of the code below!
if __name__ == "__main__":
    main()