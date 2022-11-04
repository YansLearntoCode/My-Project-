import random as rn

while True: 
    try:
        panjangpw = int(input("Masukkan Panjang Password yg Diinginkan : "))
        
        for i in range(panjangpw):
            print(chr(rn.choice(range(33, 127))), end='')
        break
    
    except ValueError:
        print("Masukkan Angka Ya Adik-Adik!")
        break