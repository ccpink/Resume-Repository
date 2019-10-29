"""
Student Name:  Geoff Gillespie  
Program Title:  Energy Calculator - BROKEN
Description:   Debugging practice
"""

def main(): #<-- Don't change this line!
    
    print("Energy Calculator")
    print("\nThis program will calculate how much you pay for electricity for")
    print("a particular device, based on the wattage of the device and how")
    print("many hours the device was in use.")
    print("\nCalculations are based on a cost of 12.65 cents per kiloWatt hour.")

    kwhPrice = 12.65
    avgDaysInAMonth = 30.42
    monthsInYear = 12

    deviceWattage = float(input("\nEnter the wattage of the device: "))
    hoursUsedPerDay = float(input("Enter how many hours per day the device is in use: "))

    #The are alot of problems with the calculations
    # Energy Consumption Cost($/day) = E(kWh/day) × Cost(cent/kWh) / 100(cent/$)
    #E(kWh/day) = P(W) × t(h/day) / 1000(W/kW)

    #This is the cost per hour so you would want to divid it by the hours used right?
    #costPerHour = ((deviceWattage /100) * kwhPrice) / hoursUsedPerDay
     deviceWattage * hoursUsedPerDay / 1000

    #BUGHERE The cost per day is not the hours used per day? I commented it out below
    #costPerDay = hoursUsedPerDay
    costPerDay = hoursUsedPerDay 

    #BUGHERE You don't need to * it by an additional 60
    costPerMonth = avgDaysInAMonth * costPerDay * 60

    #This is right
    costPerYear = monthsInYear * costPerMonth

    #BUGHERE Why is it being divided by 1000 
    #Watt-hours is Watts x Hours a day
    #kwh is Watt-hours / 100 watts
    #so in this piece he didn't finish the entire equation
    kwhPerDay = (deviceWattage /1000) * hoursUsedPerDay


    #BUGHERE Down below on the first print command I needed to change the 0 to a 1 so that hoursUsedPerDay showed up in the print command since before it was a zero and showed deviceWattage twice
    print("\nElectrical cost for a device using {0:.2f} watts for {1} hour per day:".format(deviceWattage, hoursUsedPerDay))

    #BUGHERE need to reformat all of these so they are 2 spaces to the left of the decimal
    #print("\tCost Per Hour:\t${0:.1f}".format(costPerHour))
    #print("\tCost Per Day:\t${0:.4f}".format(costPerDay))
    #print("\tCost Per Month:\t${0:.5f}".format(costPerMonth))
    #print("\tCost Per Year:\t${0:.2f}".format(costPerYear))
    #print("\tkWh Per Day:\t{0:.2f}".format(kwhPerDay))
    #What is should have been below
    print("\tCost Per Hour:\t${0:.2f}".format(costPerHour))
    print("\tCost Per Day:\t${0:.2f}".format(costPerDay))
    print("\tCost Per Month:\t${0:.2f}".format(costPerMonth))
    print("\tCost Per Year:\t${0:.2f}".format(costPerYear))
    print("\tkWh Per Day:\t{0:.2f}".format(kwhPerDay))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()