import random as rn

while True: 
    try:
        pwlen = int(input("Input the length of the password : "))
        
        for i in range(pwlen):
            print(chr(rn.choice(range(33, 127))), end='')
        break
    
    except ValueError:
        print("Input number only please!!")
        break