import random
import string
Lower = string. ascii_Lowercase
Upper = string.ascii_Uppercase
symbols = "!#@$%^&?:{}[]"
numbers = "0123456789"
all=Lower + Upper + symbols + numbers
while(True):
    print("choose an option:\n\t 1)Creat a password\n\t 2)Exit")
    choice = input("enter your choice:")
    if choice == "1":
        Length = int(input("Enter the length of password:"))
        password = "".join((random.sample(all, Length)))
        print(password)
        
    
    


