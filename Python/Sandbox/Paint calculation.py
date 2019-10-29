"""
Student Name:Charles    
Program Title:Paint Needed To Paint Walls  
Description:It has variables that can be plugged into for height and
length of both walls it then calculates the dimensions of the walls
then it calculates the combined area of the 4 walls then it divides 
it by a gallon of paint and rounds up     

https://www.dotnetperls.com/math-python Used this to understand how to round up
"""

def main():

    import math

    RoomHeight1 = 7
    RoomHeight2 = 7
    RoomLength1 = 10
    RoomLength2 = 20

    Dimensions1 = (RoomLength1*RoomHeight1)
    Dimensions2 = (RoomLength2*RoomHeight2)

    Area = (2*(Dimensions1 + Dimensions2))

    UnroundedPaint = (Area/150)

    PaintNeeded = math.ceil(UnroundedPaint)

    print("You need", PaintNeeded, "buckets worth.")



if __name__ == "__main__":
    main()

