print("WELCOME TO TREASURE ISLAND.\nYOUR MISSION IS TO FIND THE TREASURE")
option=input("Enter which way you want to go 'Left' or 'Right':")
if option=="Left":
    print("Game over")
else:
    option1=input("Do you want to swim or wait?:")
    if option1=="swim":
        print("Game over")
    else:
        option2=input("Which colour door do you choose?\n Red, Yellow, Blue?:")
        if option2=="Red":
            print("Game over")
        elif option2=="Blue":
            print("Game over")
        elif option2=="Yellow":
            print("Conrajulations, you found the treasure")
            
    
