num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
op = input("Enter the operation you wanna perform i.e '+' for addition, '-'for substaction, '*'for multiplication and '/'for division ")
if(op=="+"):
    print("Result: ",num1+num2)
elif(op=="-"):
    print("Result: ",num1-num2)
elif(op=="*"):
    print("Result: ",num1*num2)
elif(op=="/"):
    if(num2==0):
        print("Cannot be divided by 0")
    else:
        print("Result: ",num1/num2)
else:
    print("Invalid operator try again")