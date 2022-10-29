# Input: idNumber, yourHours, payRate, taxRate
# Calculate: Gross pay, Taxes owed, Netpay, Overtime pay, and Overtime hours
while True:
    idName = input("What is your name?: ")
    
    yourHours = float(input("\nHow many hours do you work in a week?: "))

    payRate = float(input("\nWhat is your hourly rate?: ")) 

    taxRate = float(input("\nWhat is your tax rate?: "))
    
    if yourHours > 40:
        ovetimeHours = yourHours - 40
        normalPay = payRate * yourHours
        ovetimePay = payRate * 1.5 * ovetimeHours
        grossPay = ovetimePay + normalPay
        taxesOwed = grossPay / taxRate
        netPay = grossPay - taxesOwed 
        
        print("\nYour name is: ",idName)
        print("Your gross pay is: ", grossPay)
        print("The amount you owe in taxes are: ", taxesOwed)
        print("Your net pay is: ", netPay)
        

    else:
        grossPay = payRate * yourHours
        taxesOwed = grossPay / taxRate
        netPay = grossPay - taxesOwed

        print("\nYour name is: ", idName)
        print("Your gross Pay is: ", grossPay)
        print("The amount you owe in taxes are: ", taxesOwed)
        print("Your net pay is: ", netPay)

    again = input("\nGo Again? (Y/N): ")
    if again == "n" or again == "no" or again == "NO" or again == "No":
        break
    


#endprogram
