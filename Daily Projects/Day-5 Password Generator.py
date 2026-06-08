import random

letters=[
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','@','#','$','%','^','&','*','(',')','_','+']

num_of_letters=int(input("How many letters do you want in your password:"))

num_of_numbers=int(input("How many numbers do you want in your password:"))

num_of_symbols=int(input("How many symbols do you want in your password:"))

password_letters=[]

password_numbers=[]

password_symbols=[]

while num_of_letters!=0:

    a=random.randint(0,51)

    password_letters.append(letters[a])

    num_of_letters-=1

while num_of_numbers!=0:

    b=random.randint(0,9)

    password_numbers.append(numbers[b])

    num_of_numbers-=1

while num_of_symbols!=0:

    c=random.randint(0,11)

    password_symbols.append(symbols[c])

    num_of_symbols-=1

password_list=password_letters+password_numbers+password_symbols

random.shuffle(password_list)

password="".join(password_list)

print("Your password is :",password)

    
    
    
    







