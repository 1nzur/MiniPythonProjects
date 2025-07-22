status = True
bal = 1000
while status==True:
    op=input("Enter the action you want to perform" \
    "i.e 1 to check balance, 2 to deposit, 3 to withdraw and 4 to exit")
    if(op=="1"):
        print(bal)
    elif(op=="2"):
        depo=int(input("Enter the amount cash you want to deposit"))
        bal = bal + depo
    elif(op=="3"):
        withdraw=int(input("Enter the amount of cash you want to withdraw"))
        if(withdraw>bal):
            print("You cannot withdraw because withdrawing amount exceeds your balance")
        else:
            bal = bal - withdraw
    elif(op=="4"):
        status = False
    else:
        print("Invalid action")