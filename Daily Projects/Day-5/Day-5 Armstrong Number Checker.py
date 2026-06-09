# Armstrong Number in Python

number=input("Enter the number you want to check:")

power=len(number)

sum=0

for i in  number:
    sum+=(int(i))**power

if str(sum)==number:
    print("Entered number is Armstrong number")

else:
    print("Number entered is not Armstrong")
