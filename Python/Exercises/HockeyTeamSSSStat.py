#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    Team_Name = input("Please enter your teams name: ")
    Team_Win = input("Please enter your teams wins: ")
    Team_Loss = input("Please enter your teams losses: ")
    print("Thank you for entering values")

    w = float(Team_Win)
    l = float(Team_Loss)
    winpercent = (w-l)/w*100
    ratio = (w/(w+l))
    Final_L = "Your team", Team_Name,"Wins", w, "Losses", l,"Ratio", "{0:.4f}".format(ratio),"Win percent", "{0:.4f}".format(winpercent)
    print(Final_L)
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()