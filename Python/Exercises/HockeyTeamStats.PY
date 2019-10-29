#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
#I'm going to need to have the user input the team name
#Probably best to use a number however to limit user interaction 
#I'm going too need to use If statements to make sure they get
#the information on the team they want we can't flood the user
# with information they don't want
# probably want variables for the team stats so they are easily changed


#Stats from https://chl.ca/

    Team1 = "|59   |8     |88.06% |"
    Team2 = "|54   |10    |84.38% |"
    Team3 = "|52   |13    |80%    |"
    Team4 = "|50   |12    |80.65% |"
    Team5 = "|46   |15    |75.41% |"
    Team6 = "|48   |15    |76.19% |"
    Team7 = "|49   |15    |76.56% |"
    Team8 = "|49   |15    |76.56% |"
    Team9 = "|47   |16    |74.6%  |"
    Team10 = "|45   |17    |72.58% |"
  #          |Win  |Loss  |Ratio  |
    #Start of program should I ask the user if they want stats? 
    #if I do I need to end the program afterwards so if/else?

    print("Hello, would you like to know stats on hockey teams.")
    YesorNo = input("Please enter Y/N: ")
    if YesorNo == 'Y':
        #User needs too know how to access the teams stats 
        print("What team would you like too know about")
        print("Rouyn-Noranda, Huskies = 1\nPrince Albert Raiders = 2\nDrummondville Voltigeurs = 3")
        print("Ottawa 67's = 4\nLondon Knights = 5\nVancouver Giants = 6")
        print("Baie-Comeau, Drakkar = 7\nHalifax, Mooseheads = 8\nEverett Silvertips = 9 ")
        print("Saginaw Spirit = 10")
        print("Each team has a number assigned to them please input that number.")
        TeamNumber = input("Please enter the team number here: ")
        #Need a way to fetch team data
        if TeamNumber == '1':
            print("|Win  |Loss  |Ratio  |")
            print(Team1)
        if TeamNumber == '2':
            print("|Win  |Loss  |Ratio  |")
            print(Team2)
        if TeamNumber == '3':
            print("|Win  |Loss  |Ratio  |")
            print(Team3)
        if TeamNumber == '4':
            print("|Win  |Loss  |Ratio  |")
            print(Team4)
        if TeamNumber == '5':
            print("|Win  |Loss  |Ratio  |")
            print(Team5)
        if TeamNumber == '6':
            print("|Win  |Loss  |Ratio  |")
            print(Team6)
        if TeamNumber == '7':
            print("|Win  |Loss  |Ratio  |")
            print(Team7)
        if TeamNumber == '8':
            print("|Win  |Loss  |Ratio  |")
            print(Team8)
        if TeamNumber == '9':
            print("|Win  |Loss  |Ratio  |")
            print(Team9)
        if TeamNumber == '10':
            print("|Win  |Loss  |Ratio  |")
            print(Team10)

        #Thank you message
        print("Thank you for using our service.")
        print("Have a nice day!")
    
    #if No
    if YesorNo == 'N':
        print("Sorry to hear that have a nice day")
        pass



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()