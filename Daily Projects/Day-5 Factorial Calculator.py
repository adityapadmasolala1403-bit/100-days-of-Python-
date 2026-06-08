#Factorial Calculator

number=int(input("Enter the number you want to calculate:"))

factorial=1

while number!=0:
    factorial*=number
    number-=1

print("The factorial is",factorial)
           
