import random

def generator(lenght):
    password=""

    for i in range(number):
        gen = random.randrange(33,127)
        password= password+chr(gen)

        
    
    print("Your password is "+ str(password))
        
    


number = int(input("Please enter NO. of characters you want to enter : "))
generator(number)




