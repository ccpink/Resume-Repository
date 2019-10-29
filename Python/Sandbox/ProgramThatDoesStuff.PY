#What do I want this program too do
#Text adventure
#What do I want it too output
#what is happening in the game
#What inputs do I need 
#The players movement
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    print("\nYou have traveled 5 years to make it too the kingdom of Anavail")
    print("Anavail is a small kingdom full of small villa's and is rather rich with culture")

    Directions = input("\nPlease input a direction, n, s, e, w: ")

    if Directions == "n":
        print("You go north towards the town straight on you see a giant gate.")
        print("The guards yell at you saying you are not allowed in, ")
        Phrase = input("What do you say back?\n(1) I traveled for 5 years to get here what the fuck \n(2)Ok I will leave\n(3)Try and jump the wall \n")
    
        if Phrase == "1":
            YesorNo = input("The guards yell down you can wait if you want but you wont get in will you look for another way in \n(Y) (N): ")
            if YesorNo == "Y":
                print("You set up a tent, while you are setting it up a snake slivers by you as your not looking and you accidentally step on it and it bites you. You scream as the venom burns through your viens and you yell for help from the guards, and they ignore you as you die")
                print("Game Over Yeah")
            else:
                Directions = input("Do you head s, w, e?: ")
        if Phrase == "2":
            Directions = input("Do you head s, w, e?: ")
        if Phrase == "3":
            print("You ready your stubby legs to try and jump and you jump and fall on your ass because you can't possibly jump that high")
            print("The guards start laughing at you")
            Directions = input("Do you head s, w, e to get away from the guards laughter?: ")
    if Directions == 'e':
        print("You go west trying too look for an alternative way into the town")
        Sword = input("You see a sword lying down do you pick it up: (y)(n)")
        if Sword == "y":
            print("You picked up the sword")
            print("You turn around just as a bear runs throught the forest at you, you just barely manage to swing your sword and kill it")
            Directions = input("You head back to the original clearing the path heading north seems to be blocked off where do you go, s w: ")
        if Sword == "n":
            print("A bear comes out of the forest and mauls you too death")
            print("Game Over Yeah")

    if Directions == 'w':
        print("You go west trying too look for an alterative way into the town")
        print("You walk across a strange hut it seems to have seen trying times.\nYou ponder who might have lived there for a second and you notice a path veering off to the right")
        Option1 = input("Do you want to head inside(i) the hut or do you wish too turn left(l): ")

        if Option1 == 'i':
            print("You see an old lady who is sitting down next too a table")
            Option2 = input("Do you walk towards(t) the old lady or do you leave(l): ")
            if Option2 == 't':
                print("She says hello")
            if Option2 == 'l':
                print("you hear her start whispering a curse behind you")
        if Option1 == 'l':
            print("Hello")

    if Directions == 's':
        print("For some reason you decide when you got this close too the town to leave")    

    else:
        print("Please Play Again!")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()