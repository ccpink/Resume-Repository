#Variables, Num of Hourse, Dollar amount they make per hour, and the over time increase and the number of hours for overtime to kick in

numOfHours = 0.0
income = 0.0
overtime = 40
overtimeincrease = 1.5
#Welcome message
print("Welcome to the wage calculator, please let us calculate your wage")

#I need to inputs one for the money they make and their how many hours they worked
income = float(input("Please input your income per hour: "))
numOfHours = float(input("Please input your number of hours worked: "))
print("Thank you for inputting the values")

#calculations since it needs to print somthing when the value is retrieved as false we might want to do an if statement
if numOfHours > overtime:
    #We need to calculate the overtime pay
    overTimeIncome =  (income)*(numOfHours * 1.5)
    print("Your total amount of money you will make is $" "{0:.2f}".format(overTimeIncome))
else:
    #We need to calculate normal pay
    incomePerHour = numOfHours * income
    print("Your total amount of money you will make is $" "{0:.2f}".format(incomePerHour))


