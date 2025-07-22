import os
print("Make sure the gusser is away from the screen")
sec = int(input("Ennter the secret number"))
os.system('cls')
num = int(input("Try to guess the number"))
while(num!=sec):
    if(num>sec):
        print("The number is smaller")
    else:
        print("The number is bigger ")
    num=int(input("Try again"))
print("Congratulations")