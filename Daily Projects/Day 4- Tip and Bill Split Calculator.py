print("TIP CALCULATOR")
bill_amount=float(input("Enter your Bill Amount:"))
total=int(input("Enter number of people:"))
tip_percentage=int(input("How much tip would you want to give? 10%,12%,15%:\n"))
total_tip=bill_amount*(tip_percentage/100)
each_tip=total_tip/total
print("The total bill is : ",bill_amount+total_tip)
print("The total tip is:",total_tip)
print("Each person has to tip:",each_tip)
print("Each person has to pay ",(bill_amount/total)+each_tip ," finally")

          
                  
